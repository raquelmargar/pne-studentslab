def fibon(n):
    s = 0
    z = 1
    for i in range(1, n + 1):
        t = s + z
        s = z
        z = t
    return s

print(f"5th fibonacci term: {fibon(5)}")
print(f"10th fibonacci term: {fibon(10)}")
print(f"15th fibonacci term: {fibon(15)}")