number_1= eval(input("Enter number 1:"))
number_2= eval(input("Enter number 2:"))
print ("1)addition 2)subtraction 3)multiplication 4)division")
j= eval(input("insert operator given above 1-4 :"))

if j==4  :
    print(number_1/number_2)
elif j==3  :
    print(number_1*number_2)
elif j==2:
    print(number_1-number_2)
elif j==1:
    print(number_1+number_2)
else:
    print("operator doesnt exist")