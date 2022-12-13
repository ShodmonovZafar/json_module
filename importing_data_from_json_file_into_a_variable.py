import json

path_to_the_json_file = "json_files/json_file.json"

with open(path_to_the_json_file, 'r') as f:
    data = json.load(f)

print(data)

