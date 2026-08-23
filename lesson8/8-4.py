def clean_name(name):
    return name.strip().lower()

print(clean_name("  John  "))  # "john"

raw_names = ["KElvin   ", "  AVA  ", "  John  ", "Paul  "]
cleaned_names = []
for name in raw_names:
    cleaned_names.append(clean_name(name))
print(cleaned_names)  # ['kelvin', 'ava', 'john', 'paul']

def count_greater_than(numbers, threshold):
    count = 0
    for number in numbers:
        if number > threshold:
            count += 1
    return count

nums = [2,4,7,9,10,3]
print(count_greater_than(nums, 5))
print(count_greater_than(nums, 9))