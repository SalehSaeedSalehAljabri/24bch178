import csv
data = [["Roll No", "Name", "Marks1", "Marks2", "Marks3"], [1, "Alice", 85, 90, 95], [2, "Bob", 78, 82, 88], [3, "Charlie", 92, 87, 85]]
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("CSV file created successfully.")
