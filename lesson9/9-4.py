def make_min_length_checker(min_length):
    def check(text):
        return len(text) >= min_length
    return check

is_long_enough = make_min_length_checker(8)

print(is_long_enough("Hello"))  # Output: False
print(is_long_enough("Hello, World!"))  # Output: True

def normalise_names(names):
    def clean_name(name):
        return name.strip().lower().capitalize()
    cleaned = []
    for n in names:
        cleaned.append(clean_name(n))
    return cleaned

raw = ["KElvin   ", "  AVA  ", "  John  ", "Paul  "]
print(normalise_names(raw))  # Output: ['kelvin', 'ava', 'john', 'paul']