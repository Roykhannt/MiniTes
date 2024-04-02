numbers = list(range(1, 101))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

for i in range(100, 0, -1):
    if i % 3 == 0 and i % 5 == 0:
        print("FooBar", end=", ")
    elif i % 3 == 0:
        print("Foo", end=", ")
    elif i % 5 == 0:
        print("Bar", end=", ")
    elif i == 1:
        print("1", end=", ")
    else:
        if is_prime(i):
            continue
        else:
            print(i, end=", ")

