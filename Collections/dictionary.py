
#mkaing dictionary of multiple data type and collection (stirng,int,list,dictionary)
a={
    "name":"marium",
    "age":25,
    "subjects":["DS","DA","DE"],
    "eductaion":{
        "BSSE":2023,
        "MS":2024,
        "PHD":2025
    }
}

print(a["name"])
print(a["age"])
print(a["subjects"])
print(a["eductaion"])

print(a["eductaion"]["MS"])  #only check dictionary value of key MS

print(a.keys())
print(a.values())
print(a.items())
print(a)
print(a.get("age"))
print(a.get("ages"))

words={
    "saniha":"accident",
    "qalam":"pen",
    "kitab":"book"
}
print("Search your Words : ",list(words.keys()))
search=input("Enter your desire word : ")
print(words.get(search))


