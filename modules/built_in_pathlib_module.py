from pathlib import Path

# We can use absolute or relative paths.
# If we don't pass an argument, the path will be the current directory
path = Path('.')
print(path.exists())
print(path.absolute())
