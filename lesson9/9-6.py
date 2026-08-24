def clamp(value, low, high):
    """
    Keep value within the inclusive range [low, high]

    if value is below low, return low
    if value is above high, return high
    otherwise return value
    """

    if value < low:
        return low
    if value > high:
        return high
    return value

print(clamp(5,0,10))
help(clamp)