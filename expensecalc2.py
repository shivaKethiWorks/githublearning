exp = [12 , 18 , 23 , 29 , 33, 39]
exp2 = [43,29]
print("before" , exp)
print("total number of items in the list" , len(exp))
exp.append(25)
print("atter" , exp)
exp.sort()
print(exp)
exp.remove(29)
print(exp)
exp.extend(exp2)
print(exp)
