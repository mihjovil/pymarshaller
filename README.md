# pymarshaller
This module is of my own creation and the purpose is to allow for a conversion between JSON objects or string 
representation of JSON into a given Dataclass from Python. The reason for this is to have an easier access to the
attributes inside a complex and nested JSON object using Python syntax.

## Limitations
I created this module after working with Golang and witnessing how simple and easy it is to perform this task is that
language. However, given Python's nature, I have not found (if such thing exist) a way to perform the whole process
automatically and programmatically. However, it can still convert a complex and nested JSON element into one or multiple
instances of a dataclass. The main difference is that it may require more than one line of code to fully convert the
JSON in to a Python object unlike the marshaller functions in Golang. That means, that if the target dataclass has
subclasses inside, in the first line these attributes will simply be a dictionary. It will require that dictionary
to be "manually" unmarshalled using the same function that was used in the first place.

## How to install?
In any python environment or virtual environment just use the following line to install:

`pip install git+https://github.com/mihjovil/pymarshaller`

## How to use?

In order to instantiate a `pymarshaller` tool, all you need is to import the module and create an Instance (It 
is intended to work on dataclasses):

```
from marshaller.pymarshaller import Pyshaller
marshaller = Pyshaller()
```
 The two important functions are:
1. Marshall: Takes a dataclass and converts it into a JSON dictionary.
2. Unmarshall: Takes a JSON dictionary and converts it into a dataclass object. The dataclass must have been declared
in order to be used.

For more information check the 
<a href="https://github.com/mihjovil/pymarshaller/blob/main/marshaller/test/test_pymarshaller.py">examples</a> in the
test files.


## License
<a href="https://choosealicense.com/licenses/mit/">MIT</a>