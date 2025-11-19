def class_average(student_dict) :

    students_averages = {}

    if not student_dict :
        return {"top students" : None,"lowest student" : None,"calss average" : None }
    
    if student_dict :

        for name,subjects in student_dict.items() :    #you can notice that i did work 2 times (students_average) that i already did in previous def fc ,i did it fo practice porpuse

            scores = list(subjects.values())
            tl_subjects = len(subjects)
            average = round(sum(scores) / tl_subjects,1)
            students_averages[name] = average

        top_student = max(students_averages, key = students_averages.get)
        low_student = min(students_averages, key = students_averages.get)
        Class_average = round(sum(students_averages.values())/ len(students_averages),1)

        if 80 <= Class_average <= 100 :
            class_grade = "A"
        elif 60 <= Class_average <= 79 :
            class_grade = "B"
        elif 50 <= Class_average <= 59 :
            class_grade = "C"
        else :
            class_grade = "F"

            
        return {"top student" : top_student,
                "lowest student" : low_student,
                "Class average" : Class_average,
                "Class grade" : class_grade
        }