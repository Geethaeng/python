"""
Write a python program to find and display the product of three positive integer values based on the rule mentioned below:
It should display the product of the three values except when one of the integer value is 7.
In that case, 7 should not be included in the product and the values to its left also should not be included.
If there is only one value to be considered, display that value itself. If no values can be included in the product, display -1.
Note: Assume that if 7 is one of the positive integer values, then it will occur only once. Refer the sample I/O given below.
"""
# code 1 - number as string

num=input("enter 3 digit positive number :")
def product_3(num):
    if (len(num)>3  or len(num)<3 or int(num)<0):
        res="enter 3 digit positive number"
    else:
        if(num[2]=='7'):
            res=-1
        elif(num[1]=='7'):
            res=num[2]
        elif(num[0]=='7'):
            res=int(num[1])*int(num[2])
        else:
            res=int(num[0])*int(num[1])*int(num[2])
    return res

prod=product_3(num)
print(prod)

# code 2 - 3 numbers as input

num1=input("enter 1 digit positive number1 :")
num2=input("enter 1 digit positive number2 :")
num3=input("enter 1 digit positive number3 :")
def product_3(num1,num2,num3):
    if ((len(num1)!=1 or len(num2)!=1 or len(num3)!=1) or (int(num1)<0 or int(num2)<0 or int(num3)<0)):
        res="enter 1 digit positive number"
    else:
        if(num3=='7'):
            res=-1
        elif(num2=='7'):
            res=num3
        elif(num1=='7'):
            res=int(num2)*int(num3)
        else:
            res=int(num1)*int(num2)*int(num3)
    return res

prod=product_3(num1,num2,num3)
print(prod)





