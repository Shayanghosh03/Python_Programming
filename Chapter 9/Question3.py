n=int(input("Enter the number:"))
def print_fact(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    print("factorial is=",f)
print_fact(n)