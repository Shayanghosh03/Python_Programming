nums=(1,4,9,16,25,36,49,54,81,100)
x=int(input("Enter the finding value:"))
i=0
for el in nums:
    if(el==x):
        print("Number found at idx",i)
        break
    i+=1
else:
    print("Value not found")
print("Code End")