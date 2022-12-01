import json

path_to_the_json_file_1 = "json_file/json_file_1.json"
path_to_the_json_file_2 = "json_file/json_file_2.json"

with open(path_to_the_json_file_1, 'r') as f:
    data_1 = json.load(f)

with open(path_to_the_json_file_2, 'r') as f:
    data_2 = json.load(f)

print(data_1)
print(data_2)
