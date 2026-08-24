def add_item(items, new_item):
    items.append(new_item)
    return items

names = ["Kelvin", "Ava", "John"]
print(names)  # Output: ['Kelvin', 'Ava', 'John']
add_item(names, "Paul")
print(names)  # Output: ['Kelvin', 'Ava', 'John', 'Paul']

def add_one(x):
    x = x + 1
    return x

n = 10
add_one(n)
print(n)

n = add_one(n)
print(n)