'''info={
"name" : "apna college",
"subjects" : ["python","java"],
"topics" :("dict","set"),
"age" :35,
"is_adult" : True,
"marks" :94.4,
45:90

}
print(info)

#dictionary is mutable
#don't allow duplicate key
info["name"]= "shristi priya"
print(info["name"])

info["surname"]="gupta"
print(info["surname"])


#empty dictionary

null_dict={}
null_dict["name"]="saaaaa"
print(null_dict)


#nested dictionary
student={
    "name" : "shristi",
    "subjects" :{
        "phy":99,
        "chem":98,
        "math":97
      
    }
  }

print(student)
print(student["name"])
print(student["subjects"])
print(student["subjects"]["chem"])

'''

#dictionary methods
info={
"name" : "apna college",
"subjects" : ["python","java"],
"topics" :("dict","set"),
"age" :35,
"is_adult" : True,
"marks" :94.4,
45:90

}

print(info.keys())
print(list(info.keys()))
print(len(list(info.keys())))


print(info.values())

print(info.items())

print(info.get("name"))  



#print(info["roll"]) #error
print(info.get("roll"))  #no error , it will return None


info.update({"city" : "patna"})
print(info)



new_dict={"code":2334,"address":"patna"}
info.update(new_dict)
print(info)