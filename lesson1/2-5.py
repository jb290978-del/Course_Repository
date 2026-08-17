#x = 39.99
#y = .0625
#z = x * y
#t = x + z
#print(t)

subtotal = float(input("Subtotal: £"))
tax_rate = float(input("Tax rate: "))
tax = subtotal * tax_rate
total = subtotal + tax
print("Total = £", str(total))