def scores(score):
    if score >= 9.0:
        return "A"
    elif 7.00 <= score <= 8.9:
        return "B"
    elif 5.0 <= score <= 6.9:
        return "C"
    elif 3.0 <= score <= 4.9:
        return "D"
    else:
        return "F"

print("Score 9.5 ->", scores(9.5))
print("Score 7.0 ->", scores(7.0))
print("Score 5.5 ->", scores(5.5))
print("Score 3.2 ->", scores(3.2))
print("Score 1.0 ->", scores(1.0))