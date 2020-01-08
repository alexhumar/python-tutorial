is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Use warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

#Otro ejemplo
price = 1000000
has_good_credit = True

#La variable down_payment se puede definir on the fly, pero hay que tener cuidado porque si no esta definida
#y se trata de acceder, python tira una excepcion
if has_good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2

print(f'Down payment: ${down_payment}')
