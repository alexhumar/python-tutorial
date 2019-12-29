course = 'Python for Beginners'
#Al string se lo puede acceder como un array
print(course[0])
#Y tambien se puede lograr una especie de truncado, de la siguiente manera:
print(course[0:3])
#Esto ultimo retorna los caracteres desde el index 0 al 3 sin incluir. En este caso, Pyt.

#Tambien acepta valores por defecto, de la siguiente manera:
print(course[0:])
#Y se puede hacer
print(course[1:])
#Y si no se le pasa el valor inicial, se asume 0
print(course[:5])

#Y el complicado, donde -1 es el indice del ultimo caracter, asi que lo descarta, asi como el primero
print(course[1:-1])
