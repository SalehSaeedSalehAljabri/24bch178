import csv
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    student_data = {}
    for row in reader:
        total = int(row["Marks1"]) + int(row["Marks2"]) + int(row["Marks3"])
        student_data[row["Roll No"]] = {"Name": row["Name"], "Marks": [row["Marks1"], row["Marks2"], row["Marks3"]], "Total": total}
print(student_data)
