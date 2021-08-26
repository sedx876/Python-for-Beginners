#> < >= <= == !=
temperature = 30

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")


name = "Jason"

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be less then 50 characters")
else:
    print("Name looks good")
