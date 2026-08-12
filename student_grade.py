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

        # Entering student names and marks for each subject
    print("\n--- Enter Student Details and Marks ---")
    for i in range(num_students):
        name = input(f"\nEnter name for Student {i+1}: ").strip()
        if not name:
            name = f"Student {i+1}"
        student_names.append(name)
        for j in range(num_subjects):
            while True:
                try:
                    mark = float(input(f"  Enter marks for {name} in Subject {j+1} (out of 100): "))
                    if 0 <= mark <= 100:
                        marks_array[i, j] = mark
                        break
                    else:
                        print("  Marks should be between 0 and 100. Please try again.")
                except ValueError:
                    print("  Invalid input. Please enter a numerical value for marks.")