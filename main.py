from student_data import student_data
from student_average import student_average
from class_average import class_average
from datetime import datetime
import json

student = student_data()

Student_Average = student_average(student)
Class_Average   = class_average(student)

now = datetime.now()
time = now.strftime("%Y-%m-%d %H:%M:%S")

Data = {"students_data" : student, "student average" : Student_Average, "Class average" : Class_Average}

with open("report.json", "w") as file:
    json.dump(Data, file, indent=4)

with open("report.txt", "w") as file:
    file.write(f"Report generated at: {time}\n\n")
    file.write("Students Data:\n")
    for name, scores in student.items():
        file.write(f"  {name}: {scores}\n")

    file.write("\nStudent Averages:\n")
    for name, avg in Student_Average["averages"].items():
        file.write(f"  {name}: {avg}\n")

    file.write(f"\nClass Average: {Class_Average['Class average']}\n")
    file.write(f"Class Grade: {Class_Average['Class grade']}\n")
    file.write(f"Top Student: {Class_Average['top student']}\n")
    file.write(f"Lowest Student: {Class_Average['lowest student']}\n")


print("results",Data)