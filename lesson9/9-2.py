def compute_tax_and_total(price, tax_rate=.0625):
    """
    Computes the tax and total price based on the given price and tax rate.

    Parameters:
    price (float): The original price of the item.
    tax_rate (float): The tax rate as a decimal (e.g., 0.07 for 7%).

    Returns:
    tuple: A tuple containing the computed tax and total price.
    """
    tax = price * tax_rate
    total = price + tax
    return tax, total

tx, tl = compute_tax_and_total(100, .1)
print(tx)
print(tl)