def student_data():
    students = {}

    while True:
        name = input("Enter student name, 'Done' to finish, 'Exit' to quit: ").strip()

        if name.capitalize() == 'Exit':
            print("The program is closed, Bye !")
            break

        if name.capitalize() == 'Done':
            break

        if name == "":
            print("Enter a valid name !")
            continue

        if name not in students:
            students[name] = {}

        while True:
            subject = input(f"Subject of {name} ('Done' to finish): ").strip()

            if subject.capitalize() == 'Done':
                break

            if subject == "":
                print("Enter a valid subject !")
                continue

            try:
                score = int(input(f"Score of {name} in {subject}: "))
                if score < 0:
                    print("Score can't be negative!")
                    continue
            except ValueError:
                print("Enter a valid number!")
                continue

            students[name][subject] = score

    return students
