def student_average(student_dict):

    student_averages = {}

    if not student_dict:
        return {"averages": {}, "number of students": 0}

    for name, subjects in student_dict.items():
        scores = list(subjects.values())
        number_of_scores = len(scores)
        avg = round(sum(scores) / number_of_scores, 1)
        student_averages[name] = avg

    return {
        "averages": student_averages,
        "number of students": len(student_averages)
    }
