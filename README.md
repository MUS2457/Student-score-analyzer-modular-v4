Features

Add multiple students and their subject scores

Calculate student averages

Determine class average and grade

Identify top and lowest student

Generate JSON and TXT reports

Fully modular functions for maintainability

Handles invalid input gracefully

Installation

Clone the repository:

git clone https://github.com/yourusername/student-score-analyzer-v4.git


Navigate to the folder:

cd student-score-analyzer-v4


Run the program:

python main.py

Usage

Enter student names, subjects, and scores

Type Done to finish adding subjects

Type Done or Exit to finish adding students

JSON and TXT reports are automatically generated:

report.json

report.txt

Example output in terminal:

{
    "students_data": {
        "Amine": {"Math": 90, "English": 85}
    },
    "student average": {"averages": {"Amine": 87.5}, "number of students": 1},
    "Class average": {"top student": "Amine", "lowest student": "Amine", "Class average": 87.5, "Class grade": "A"}
}
Technologies

Python 3

JSON for data persistence
