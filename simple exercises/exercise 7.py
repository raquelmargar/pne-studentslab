student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}

print("Name:", student["name"])
print("Number of subjects:", len(student["subjects"]))

if "PNE" in student["subjects"]:
    print("Enrolled in PNE: True")
else:
    print("Enrolled in PNE: False")

marks = student["grades"]
print("Databases grade:", marks["Databases"])

total_sum = 0
count = 0
for subject in marks:
    total_sum = total_sum + marks[subject]
    count = count + 1

media = total_sum / count
print("Average grade:", round(media, 2))

print("Subject grades:")
for subject, grade in student["grades"].items():
    print(" ", subject + ":", grade)