nums=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter the searching number:"))
i=0
while i<len(nums):
    if(nums[i]==x):
        print(x,"Number is found in idx",i)
    else:
        print("Finding!!!")
    i+=1
print("Code End")