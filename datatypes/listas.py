#Las listas pueden contener elementos de diferentes tipos y son estructuras mutables. Es decir, que pueden cambiar en ejecucion.
lista = [ 30, "Treinta", 30.0 ]
lista.append(True)
print(lista)
print(lista[0]) #Imprime 30
print(lista.index(30)) #Imprime 0
print(type(lista))