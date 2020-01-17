from pathlib import Path

# We can use absolute or relative paths.
# If we don't pass an argument, the path will be the current directory
path = Path('.')
print(path.exists())
print(path.absolute())

# Files and directories
print(path.glob('*'))
# Only files
print(path.glob('*.*'))
# The methods above return a generator object. I NEED TO INVESTIGATE THE SUBJECT.

# Prints all the .py files in the current directory
for file in path.glob('*.py'):
    print(file)
