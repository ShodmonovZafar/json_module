import json

data_1 = {}

for i in range(1, 13):
    data_1[i] = 0
    
data_2 = {
    'foo': 'bar',
    'alice': 1,
    'wonderland': [1, 2, 3]
}

path_to_the_json_file_1 = "json_file/json_file_1.json"
path_to_the_json_file_2 = "json_file/json_file_2.json"

with open(path_to_the_json_file_1, 'w') as f:
    json.dump(data_1, f)

with open(path_to_the_json_file_2, 'w') as f:
    json.dump(data_2, f)
