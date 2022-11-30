import json
d = {
    'foo': 'bar',
    'alice': 1,
    'wonderland': [1, 2, 3]
}
with open("file_name.txt", 'w') as f:
    json.dump(d, f)
