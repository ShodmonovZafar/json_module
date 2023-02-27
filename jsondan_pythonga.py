import json

json_data1 = """{
  "employee0": {
    "firstName": "John",
    "lastName": "Smith",
    "age": 35,
    "city": "San Francisco"
  },
  "employee1": {
    "firstName": "Zoe",
    "lastName": "Thompson",
    "age": 32,
    "city": "Los Angeles"
  }
}"""

with open("text_files/text_file1.txt", "w") as file:
    file.write(json_data1)
    

data1 = json.loads(json_data1)

path1 = "text_files/text_file1.txt"
path2 = "json_files/json_file1.json"

with open(path1) as file:
    json_string = file.read()
    data2 = json.loads(json_string)

with open(path1) as file:
    data3 = json.load(file)

with open(path2) as file:
    data4 = json.load(file)

with open(path2) as file:
    json_string = file.read()
    data5 = json.loads(json_string)
