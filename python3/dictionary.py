data = {"Anirudha": 33, "Vikash": 35, "Ramesh": "not a student"}
print(data)

for first, second in data.items():
    print(f"Key: {first}, Value: {second}")

print("Print keys in the dictionary: ")
for key in data.keys():
    print(key)

print("Print values in the dictionary: ")
for val in data.values():
    print(val)

# add new key-value pair in the dictionary
data[4] = 5
print(data)

print(f"Anirudha's age is {data['Anirudha']}")
