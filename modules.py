# A module is a file with some python code. We use modules to organize our code into multiple files. Each module
# should contain related functions and classes
# Check file converters.py

# With this, we import module converters from functions package, and now converters is an object
from functions import converters
# We also can import specific functions of a module. Since converters is in package functions, we must prefix the
# package name too.
from functions.converters import lbs_to_kg

print(converters.kg_to_lbs(75))
print(converters.lbs_to_kg(160))
print(lbs_to_kg(160))
