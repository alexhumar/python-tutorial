has_high_income = True
has_good_credit = True

# And or operators
if has_high_income and has_good_credit:
    print("Eligible for loan")

if has_high_income or has_good_credit:
    print("Eligible for loan (or)")

has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for loan without criminal record")

# <, <=, ==, !=, >, >= operators
temperature = 30

if temperature > 30:
    print("It's a hot day")
# Is equivalent to temperature <= 30 and temperature >= 18
elif 30 >= temperature >= 18:
    print("It's a lovely day")
elif temperature == 17:
    print("It's a great day")
else:
    print("It's a cold day")
