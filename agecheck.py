name = input("what is your name? ")
age = int(input("how old are you? "))
yearsto50 = 50 - age

if yearsto50>0:
    print(f"hello {name}, you will be 50 in {yearsto50} years")
else:
    print(f"hello {name}, you were 50 {-yearsto50} years ago")
print("bye")

