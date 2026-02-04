def fibon(n):
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c
    return a

print("The fifth element of the fibonacci serie: ", fibon(5))
print("The tenth element of the fibonacci serie: ", fibon(10))
print("The fifteenth element of the fibonacci serie: ", fibon(15))