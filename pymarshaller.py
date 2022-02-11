import json
from dataclasses import dataclass
from abc import ABC, abstractmethod
import typing
import os

@dataclass(order=True)
class Name:
    name:str
    age: int

    def __str__(self):
        return f'{self.name}: {self.age} years'


@dataclass(order=True)
class TestClass:
    age: int =None
    name: str =None
    mail: str =None
    status: bool =None
    friends: typing.List[Name]=None

    def __str__(self) -> str:
        print(type(self.friends[0]))
        friend_text = "\n".join(str(f) for f in self.friends)                    
        return f'{self.name} is {self.age} and has {len(self.friends)} friends. These are: {friend_text}'

class Pyshaller():

    def __init__(self):
        self.nothing = None

    def unmarhall(self, struct: object, json_dict: typing.Dict):
        attributes = [a for a in dir(struct) if not a.startswith('__')]
        for a in attributes:
            if a in json_dict.keys():
                try:
                    value = json_dict[a]
                    setattr(struct, a, value)
                except ValueError:
                    print(f'There is no {a} key in the dictionary')
        print(struct)



if __name__ == "__main__":
    p = Pyshaller()
    t = TestClass()
    with open('./marshaller/utils/example_input.json') as content:
        json_dict = json.load(content)
        p.unmarhall(t, json_dict)