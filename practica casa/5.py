def fibosum(n):
    sumn = 0
    s = 0
    z = 1
    for i in range(1, n + 1):
        t = s + z
        s = z
        z = t
        sumn += s
    return sumn

print(f"Sum of the first 5th terms of the fibonacci series: {fibosum(5)}")
print(f"Sum of the first 10th terms of the fibonacci series: {fibosum(10)}")
