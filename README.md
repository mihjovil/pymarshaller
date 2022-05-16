# pymarshaller
This module is of my own creation and the purpose is to allow for a conversion between JSON objects or string 
representation of JSON into a given Dataclass from Python. The reason for this is to have an easier access to the
attributes inside a complex and nested JSON object using Python syntax.

## Limitations
I created this module after working with Golang and witnessing how simple and easy it is to perform this task is that
language. However, given Python's nature, I have not found (if such thing exist) a way to perform the whole process
automatically and programatically. However, it can still convert a complex and nested JSON element into one or multiple
instances of a dataclass. The main difference is that it may require more than one line of code to fully convert the
JSON in to a Python object unlike the marshaller functions in Golang. That means, that if the target dataclass has
subclasses inside, in the first line these attributes will simply be a dictionary. It will require that dictionary
to be "manually" unmarshalled using the same function that was used in the first place.

