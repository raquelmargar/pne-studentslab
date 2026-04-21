students = [
    {"name": "Ana", "grades": [8.5, 7.0, 9.0]},
    {"name": "Luis", "grades": [5.0, 4.5, 6.0]},
    {"name": "Maria", "grades": [9.5, 9.0, 10.0]},
    {"name": "Pedro", "grades": [3.0, 4.0, 2.5]},
    {"name": "Sofia", "grades": [7.0, 7.5, 8.0]},
]


def average(grades):
    total_sum = 0
    count = 0
    for grade in grades:
        total_sum = total_sum + grade
        count = count + 1
    return total_sum / count


def get_status(avg):
    if avg >= 5.0:
        return "PASS"
    else:
        return "FAIL"

passed_count = 0
failed_count = 0

for student in students:
    name = student["name"]
    marks = student["grades"]

    media = average(marks)
    rounded_media = round(media, 1)
    status = get_status(rounded_media)

    if status == "PASS":
        passed_count = passed_count + 1
    else:
        failed_count = failed_count + 1

    print(name + ":", rounded_media, "->", status)


print("Results:", passed_count, "passed,", failed_count, "failed")