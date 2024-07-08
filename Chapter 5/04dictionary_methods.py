student={
    "name": "Shayan Ghosh",
    "score": {
        "chem": 91,
        "phy": 90,
        "math": 89
    }
}
print(student)
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
print(student["name"])

print(student.get["name2"])
#print(student["name"]) Error
 
student.update({"age": 21})
print(student)
new_dict={"city": "Barrackpore"}
student.update(new_dict)
print(student)

