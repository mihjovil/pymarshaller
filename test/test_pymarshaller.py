import unittest
from ..utils.example.example_classes import Friend, Address, Person
import typing
from pymarshaller import Pyshaller
import json

# TODO: Add the unmarshalling test

# region helper functions
def createPyshaller() -> Pyshaller:
    return Pyshaller()

def read_json_file(path: str) -> typing.Dict:
    """[summary]

    Args:
        path (str): [description]

    Returns:
        typing.Dict: [description]
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
        friend_1 = Friend("Elmo", address_1, "3111123", 6, "Unknown")
        friend_2 = Friend("Cookie monster", address_2, "3111122", 4, "Unknown")
        person = Person([friend_1, friend_2], "Enrique", 5, "3142334", address, "Male", "henry@sesame.us")

        json_answer = p.marshall(person)
        self.assertIsNotNone(json_answer)
        self.assertNotEqual(0, len(json_answer.keys))
        print(json_answer)