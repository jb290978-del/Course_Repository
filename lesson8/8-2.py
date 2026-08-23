def compute_total(price, tax_rate=.0625):
    tax = price * tax_rate
    total = price + tax
    return total

print(compute_total(100))  # Default tax rate
print(compute_total(100, 1))  # Custom tax rate
print(compute_total(price=100, tax_rate=.1))  # Custom tax rate