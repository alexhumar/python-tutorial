#Cualquier cosa que se ingresa desde la terminal se trata como string, por mas que sean números.
# Por eso hay que castear.
birth_year = input("Birth year: ")
print(type(birth_year))
age = 2019 - int(birth_year)
print(type(age))
print(age)
