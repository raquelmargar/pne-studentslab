def is_even(number):
    if number % 2 == 0:
        return "True"
    else:
        return "False"

print("is_even(4) = ", is_even(4))
print("is_even(7) = ", is_even(7))
print("is_even(0) = ", is_even(0))
print("is_even(-3) = ", is_even(-3))
print("is_even(10) = ", is_even(10))

def classify_triangle(a, b, c):
    if a == b == c:
        return "equilateral"
    elif a == b or b == c or c == a:
        return "isosceles"
    else:
        return "scalene"

print("classify triangle(5, 5, 5) = ", classify_triangle(5, 5, 5))
print("classify triangle(3, 3, 4) = ", classify_triangle(3, 3, 4))
print("classify triangle(3, 4, 5) = ", classify_triangle(3, 4, 5))