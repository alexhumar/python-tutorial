try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
    print(risk)
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Age can not be zero")
finally:
    print("End of calculation")
