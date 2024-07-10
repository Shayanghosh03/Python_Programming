with open("practice.txt","r") as f:
    data=f.read()
new=data.replace("Python","Java")
print(new)
with open("practice.txt","w") as f:
    f.write(new)