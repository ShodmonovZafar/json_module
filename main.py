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

data1 = json.loads(json_data1)

path1 = "json_files/json_file1.json"
with open(path1) as f:
    data2 = json.load(f)

path2 = "text_files/text_file1.txt"
with open(path2) as f:
    data3 = json.load(f)

data4 = ['text', False, {"0":None, 1:[1.0, 2.0]}]
json_data2 = json.dumps(data4, indent=4)
print(json_data2)

