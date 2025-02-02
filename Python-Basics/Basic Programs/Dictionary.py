info={
    "name": "Abbas",
    "lastName":"Ali",
    "Score":[4,5,3]

}
null_dict={}
print(type(null_dict))
print(info.values())
print(info.keys())
print(info.items())
print(info.get("name"))
new_dict={"city":"Khp","age": 34}
info.update(new_dict)
print(info.values())