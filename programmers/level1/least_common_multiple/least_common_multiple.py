import math

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

if __name__ == "__main__":
    print(lcm(6, 8))  
    print(lcm(12, 18))  
