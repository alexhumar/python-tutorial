# A module is a file with some python code. We use modules to organize our code into multiple files. Each module
# should contain related functions and classes
# Check file converters.py

# With this, we import module converters, and now converters is an object
import converters
# We also can import specific functions of a module
from converters import lbs_to_kg

print(converters.kg_to_lbs(75))
print(converters.lbs_to_kg(160))
print(lbs_to_kg(160))
