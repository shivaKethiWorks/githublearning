print ("hello world")

# N1=int(input("enter the N1 "))
# N2=int(input("enter the N2 "))
# print("Addition of ", N1 ,"and ", N2, "is : ", N1   + N2  )

# M1=int(input("enter M1"))
# M2=int(input("enter M2"))
# Print("")
#Write a banana republic discount application, User enters Selleing price, Give inital 50% discount and extra 25%)

TotalAmount = int(input("Enter the value of selling price  : "))
Discount = 0.5 * TotalAmount
NetAfterDiscount1 = TotalAmount - Discount
Discount2 = NetAfterDiscount1 * 0.25
NetAmount = NetAfterDiscount1 - Discount2
print ("Amount to be paid after discounts :"  , NetAmount  )
 