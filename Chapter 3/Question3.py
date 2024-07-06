a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
c=int(input("Enter the 3rd number: "))
if(a>=b and a>=c):
    max=a
elif(b>=c):
    max=b
else:
    max=c
print("Maximum of three numbers are:",max)