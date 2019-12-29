weight = float(input("Enter your weight: "))
weight_unit = input("(L)bs or (K)g: ")
lbs_in_kilogram = 0.4535920

if weight_unit.upper() == "L":
    print(f"You are {weight * lbs_in_kilogram} kg")
else:
    print(f"You are {weight / lbs_in_kilogram} lbs")
