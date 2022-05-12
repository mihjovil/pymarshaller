import typing


class Pyshaller:

    def __init__(self):
        # Constant types that are simple to marshall
        self.simple_types = [
            'str',
            'bool',
            'float64',
            'int32',
            'int64',
            'int',
            'None',        
            'datetime'            
        ]

    def is_simple(self, candidate: typing.Any) -> bool:
        """This function takes a specific type for parameter and decides whther it is a simple type or not

        Args:
            candidate (typing.Any): The candidate type to check if it is simple or not

        Returns:
            bool: True if the type is simple and should be added löike that to the JSON object or False if not.
        """
        for t in self.simple_types:
            if t in str(candidate):
                return True
        return False

    def unmarshall(self, struct: object, json_dict: typing.Dict) -> object:
        """This function takes a dataclass obejtc as well as a JSON in dictionary form. It takes all the fields in the dataclass and tries to match them to the elements in the JSON object

        Args:
            struct (object): The specific Dataclass that will be filled with the values of the JSON object.
            json_dict (typing.Dict): The JSON object that contains the values of the dataclass.

        Returns:
            object: Returns an initilized dataclass of the same type as struct with the values that it could get out of the JSON dictionary.
        """
        attributes = [a for a in dir(struct) if not a.startswith('__')]
        for a in attributes:            
            if a in json_dict.keys():
                try:
                    value = json_dict[a]
                    setattr(struct, a, value)
                except ValueError:
                    print(f'There is no {a} key in the dictionary')
        return struct

    def unmarshall_list(self, struct: object, objects: typing.List[typing.Dict]) -> typing.List[object]:
        """This method takes a list of objects in dictionary format and uses their values to fill a list of specified dataclasses that will return as answer

        Args:
            struct (object): The specified dataclass that will be filled using the values of the elements in the list of dictionaries
            objects (typing.List[typing.Dict]): The list of dictionaries that will be unmarshall to create a list of dataclasses

        Returns:
            typing.List[object]: A list of data classes that contain the values from the list of dictionaries.
        """
        answer = []
        for item in objects:
            temp_struct = struct()
            answer.append(self.unmarshall(temp_struct, item))
        return answer

    def marshall(self, struct: object) -> typing.Dict:
        """Takes a dataclass and transforms it into a Dictionary in order to be used as JSON

        Args:
            struct (object): The dataclass instance that will transformed into a dictionary.

        Returns:
            typing.Dict A dictionray that contains the values form the dataclass object (struct).
        """ 
        answer = {}
        answer = self.add_attributes_to_dict(answer, struct)
        return answer    

    def add_attributes_to_dict(self, target: typing.Dict, struct: object) -> typing.Dict:
        """This method takes a list of objects in dictionary format and uses their values to fill a list of specified dataclasses that will return as answer

        Args:
            target (typing.Dict): The dictionary struct where the values will be stored
            struct (object): The dataclass instance that will transformed into a dictionary.
        Returns:
            typing.Dict: The dictionary (target) with the values from the dataclass (struct)
        """  
        attributes = [a for a in dir(struct) if not a.startswith('__')]
        for attr in attributes:
            attr_type = type(getattr(struct, attr))
            attribute = getattr(struct, attr)
            if self.is_simple(attr_type):
                target[attr] = attribute
            elif str(attr_type).__contains__('list'):
                temp_list = []
                for e in attribute:
                    temp_dict = {}
                    if self.is_simple(type(e)):
                        temp_list.append(e)
                    else:
                        temp_list.append(self.add_attributes_to_dict(temp_dict, e))
                target[attr] = temp_list
            else:
                # It is a dictionary
                temp_dict = {}
                target[attr] = self.add_attributes_to_dict(temp_dict, attribute)
        return target
        