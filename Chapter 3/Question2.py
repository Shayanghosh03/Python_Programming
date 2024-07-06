a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
c=int(input("Enter the 3rd number: "))
if(a>b):
    if(a>c):
        max=a
    else:
        max=c
else:
    if(b>c):
        max=b
    else:
        max=c
print("Maximum number is:",max)