from output import Output


def main():
    smm = StudentMarkManagement()
    smm.input_student_information()
    smm.input_course_information()

    while True:
        print("\n1. Input student marks")
        print("2. List students")
        print("3. List courses")
        print("4. Show student marks")
        print("5. Display gpa")
        print("6. Sort students gpa")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            smm.input_student_marks()
        elif choice == 2:
            smm.list_students()
        elif choice == 3:
            smm.list_courses()
        elif choice == 4:
            smm.show_student_marks()
        elif choice == 5:
            smm.calculate_gpa()
        elif choice == 6:
            smm.sort_student_by_gpa()
        elif choice == 7:
            break
if __name__ == "__main__":
    main()