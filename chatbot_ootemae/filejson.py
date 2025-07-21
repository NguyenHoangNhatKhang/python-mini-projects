import json 

data = {
    "name":"john",
    "age":30,
}

with open("ex.json","w") as file:
    json.dump(data,file)
