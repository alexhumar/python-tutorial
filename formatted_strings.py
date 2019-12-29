first_name = 'Alex'
last_name = 'Humar'
#Funciona pero es tedioso de escribir
message = first_name + ' [' + last_name + '] is a coder.'
print(message)

#Para clarificar, se usan los formatted strings, donde se definen anteponiendo una f:
msg = f'{first_name} [{last_name}] is a coder.'
print(msg)

#Hay funciones predefinidas de proposito general que podemos usar con strings, por ejemplo:
print(len(msg))
#Pero tambien el tipo string define sus propias funciones, denominadas metodos.
print(msg.upper())
print(msg.lower())
#Retorna el indice de la primer ocurrencia del string recibido por parametro. Devuelve -1 si no lo encuentra.
print(msg.find('Hum'))
print(msg.replace('coder', 'super programmer'))
#Se puede utilizar el operador in para armar una expresion booleana:
print('coder' in msg)
print('Coder' in msg)
