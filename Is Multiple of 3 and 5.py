"""
Write a python program that displays a message as follows for a given number:
1. If it is a multiple of three, display "Zip"
2. If it is a multiple of five, display "Zap".
3. If it is a multiple of both three and five, display "Zoom".
4. If it does not satisfy any of the above given conditions, display "Invalid".
"""
num=int(input("enter number :"))
def is_multiple_3_5(num):
    if(num%3==0 and num%5==0):
        result="Zoom"
    elif(num%5==0):
        result="Zap"
    elif(num%3==0):
        result="Zip"
    else:
        result="Invalid"
    return result
ismultiple=is_multiple_3_5(num)
print(ismultiple)

