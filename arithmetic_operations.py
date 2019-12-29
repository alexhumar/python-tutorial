#Las operaciones +, - y * son triviales...
#Por otro lado, hay dos tipos de division: una que retorna como resultado un float, y otra que retorna un entero.
#Float
print(10 / 3)
#Entero
print(10 // 3)
#Se puede calcular el modulo (el resto de la division)
print(10 % 3)
#De esta manera se calcula la potencia
print(10 ** 3)
#Tambien se provee "augmented assignment"
x = 10
x += 3
print(x)
#Tambien se provee para las operaciones de resta y multiplicacion
x -= 3
x *= 2
print(x)
#PRECEDENCIA DE LOS OPERADORES (orden de las operaciones)
y = 10 + 3 * 2
#El operador * tiene una mayor precedencia, por lo que se ejecuta primero
print(y)
#Lista de ordenes de precedencia:
# 0) Parentesis.
# 1) Potencia: 2 ** 3.
# 2) Multiplicacion o division.
# 3) Suma o resta.
y = 10 + 3 * 2 ** 2
print(y)
