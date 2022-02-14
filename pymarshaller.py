import json
import typing


class Pyshaller():

    """
    TODO
    Add an unmarshall list function that reads every element in the list and creates the dataclass from it returning a list of the object
    Add the marshall function (That should be easier and recursive)
    """

    def __init__(self):
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
        for t in self.simple_types:
            if t in str(candidate):
                return True
        return False

    def unmarshall(self, struct: object, json_dict: typing.Dict) -> object:
        # Dictionary of possible attributes of object
        attributes = [a for a in dir(struct) if not a.startswith('__')]
        for a in attributes:
            print(type(json_dict))
            if a in json_dict.keys():
                try:
                    value = json_dict[a]
                    setattr(struct, a, value)
                except ValueError:
                    print(f'There is no {a} key in the dictionary')
        return struct

    def unmarshall_list(self, struct: object, objects: typing.List[typing.Dict])-> typing.List[object]:    
        answer = []
        for item in objects:
            temp_struct = struct()
            answer.append(self.unmarshall(temp_struct, item))
        return answer

    def marshall(self, struct: object) -> typing.Dict:       
        answer = {}
        answer = self.add_attributes_to_dict(answer, struct)
        return answer    


    def add_attributes_to_dict(self, target: typing.Dict, struct: object) -> typing.Dict:        
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
        