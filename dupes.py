import json
with open('seeds.json', 'r') as file:
    data = json.load(file)
# Convert dictionary keys to a list to eliminate duplicates
keys_list = list(data.keys())
data = {key: data[key] for key in keys_list}
with open('seeds.json', 'w') as file:
    json.dump(data, file, indent=4)