def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    else:
        return gcd(a, b-a)

def lcm(a, b):
    # This function returns Least Common Multiple(LCM) of integer a and b.
    return (a*b)/gcd(a, b)
