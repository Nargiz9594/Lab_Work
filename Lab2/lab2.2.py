def power(a, b):
    return a**b

try:
    print(power(*list(map(int, input("Type numbers:").split()))))
    a, b = map(int, input("Type numbers:").split())
    print(a, b)
except TypeError:
    print("Too much numbers!")
