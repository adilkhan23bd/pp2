

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]


print("Enumerate example:")
for index, name in enumerate(names):
    print(index, name)

print()


for index, name in enumerate(names, start=1):
    print(index, name)

print()


print("Zip example:")
for name, score in zip(names, scores):
    print(name, score)

print()


print("Zip + Enumerate:")
for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"{i}. {name} - {score}")