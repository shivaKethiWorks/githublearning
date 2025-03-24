#i = 1
#while i<=100:
    #print(i)
    #i = i + 1






exp = -1
total = 0
maxexp = 0
minexp = 0

while exp != 0:
    exp = int(input("what is expense? (type 0 to stop) "))
    total = total + exp
    if exp > maxexp:
        maxexp = exp
    if exp < minexp:
        minexp = exp

print(f"your total expenditure is {total}")
print(f"the maximum you spent is {maxexp}")
print(f"the minimum you spent is {minexp}")
