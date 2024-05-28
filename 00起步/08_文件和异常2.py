import json

numbers = {'name': 'lala', 'age': 20}

filename = 'text_files/numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
