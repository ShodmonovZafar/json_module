import json

data1 = ['text', False, {"0": None, 1: [1.0, 2.0]}]

json_data1 = json.dumps(data1)
json_data2 = json.dumps(data1, indent=4)

path1 = "json_files/json_file2.json"
path2 = "text_files/text_file2.txt"

with open(path1, "w") as file:
    json.dump(data1, file)

with open(path2, "w") as file:
    json.dump(data1, file)