from dataclasses import dataclass
import typing

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
