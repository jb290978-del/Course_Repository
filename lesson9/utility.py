def clean_name(name):
    return name.strip().lower().capitalize()

def compute_total(price, tax_rate=.0625):
    return price + (price*tax_rate)