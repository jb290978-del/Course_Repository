def is_passing(score):
    return score >= 60

print(is_passing(75))  # True
print(is_passing(50))  # False

def safe_divide(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a / b

print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # Error message and None