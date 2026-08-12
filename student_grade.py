import numpy as np
def calculate_grades():
    print("=" * 50)
    print("       STUDENT GRADE CALCULATOR (NumPy)")
    print("=" * 50)

    try:
        num_students = int(input("Enter the number of students: "))
        num_subjects = int(input("Enter the number of subjects: "))
        if num_students <= 0 or num_subjects <= 0:
            print("Number of students and subjects must be greater than zero.")
            return
    except ValueError:
        print("Invalid input. Please enter integer values.")
        return

    marks_array = np.zeros((num_students, num_subjects))
    student_names = []