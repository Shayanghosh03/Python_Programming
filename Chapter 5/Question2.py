marks={}
x=int(input("Enter phy:"))
marks.update({"phy":x})
x=int(input("Enter eng:"))
marks.update({"eng":x})
x=int(input("Enter chem:"))
marks.update({"chem":x})
print(marks)
print(type(marks))