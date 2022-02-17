from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))
import unittest
from utils.example.example_classes import Friend, Address, Person
import typing
from pymarshaller import Pyshaller
import json

# region helper functions
def createPyshaller() -> Pyshaller:
    return Pyshaller()

def read_json_file(path: str) -> typing.Dict:
    """ Takes a path from a JSON file, reads the content and returns a dictionary with the values from the file
    Args:
        path (str): the path of the file that will be read

    Returns:
        typing.Dict: A python dictionary with the content from the JSON file
    """
    with open(path) as content:
        json_dict = json.load(content)
    return json_dict
# endregion


class TestPymarshaller(unittest.TestCase):

    def test_marshall(self):
        p = createPyshaller()
        address = Address("Sesame street", "", 31134, "Hollywood", "USA", "4")
        address_1 = Address("Sesame street", "", 31134, "Hollywood", "USA", "3")
        address_2 = Address("Sesame street", "", 31134, "Hollywood", "USA", "2")
        hobbies_1 = ["singing", "teaching"]
        hobbies_2 = ['eating coockies']
        friend_1 = Friend("Elmo", address_1, "3111123", 6, "Unknown", hobbies_1)
        friend_2 = Friend("Cookie monster", address_2, "3111122", 4, "Unknown", hobbies_2)
        person = Person([friend_1, friend_2], "Enrique", 5, "3142334", address, "Male", "henry@sesame.us")

        json_answer = p.marshall(person)
        self.assertIsNotNone(json_answer)
        self.assertNotEqual(0, len(json_answer.keys()))
        print(json_answer)

    def test_unmarshall(self):
        p = createPyshaller()
        json_dict = read_json_file('utils/example/example_input.json')
        target = Person()
        p.unmarshall(target, json_dict)
        self.assertIsNotNone(target, "The dataclass is still None after unmarshall")
        self.assertIsNotNone(target.friends, "friends is still None")
        friends_type = type(target.friends[0])
        target.friends = p.unmarshall_list(Friend, target.friends)
        self.assertNotEqual(friends_type, type(target.friends[0]))
        address_type = type(target.address)
        target.address = p.unmarshall(Address(), target.address)
        self.assertNotEqual(address_type, type(target.address))
        print(target)

if __name__ == '__main__':
    unittest.main()