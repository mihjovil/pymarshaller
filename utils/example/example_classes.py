from dataclasses import dataclass
import typing


@dataclass
class Address:
    street: str = None
    additional_line: str = None
    postcode: int = None
    city: str = None
    country: str = None
    house_number: int = None

@dataclass
class Friend:
    name: str = None
    address: Address = None
    phone: str = None
    age: int = None
    sex: str = None
    hobbies: typing.List[str] = None

@dataclass
class Person:
    friends: typing.List[Friend] = None
    name: str = None
    age: int = None
    phone: str = None
    address: Address = None
    sex: str = None
    mail: str = None
