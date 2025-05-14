def get_student_data():
    students = []
    num_students = int(input("Enter the number of students: "))
    for i in range(num_students):
        name = input(f"Enter the name of student {i + 1}: ")
        marks = []
        for j in range(6):
            mark = float(input(f"Enter marks for subject {j + 1}: "))
            marks.append(mark)
        students.append({"name": name, "marks": marks})
    return students

def calculate_total_and_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

def calculate_grade(average):
    if average > 90:
        return 'A'
    elif average > 80:
        return 'B'
    elif average > 70:
        return 'C'
    elif average > 60:
        return 'D'
    elif average > 50:
        return 'E'
    else:
        return 'F'

def display_grade_sheet(students):
    print("\n\t\t\t\t\tGrade Sheet")
    print("|S.No\t|Name\t\t|Subject 1\t|Subject 2\t|Subject 3\t|Subject 4\t|Subject 5\t|Subject 6\t|Total\t|Average |Grade\t|")
    print("-" * 140)
    for i, student in enumerate(students):
        total, average = calculate_total_and_average(student["marks"])
        grade = calculate_grade(average)
        mark = "\t\t|".join(map(str, student["marks"]))
        print(f"|{i + 1}\t|{student['name']}\t\t|{mark}\t\t|{total}\t|{average:.2f}\t |{grade}\t|")
    print("-" * 140)

print("Welcome to the Student Grading System")
students = get_student_data()
display_grade_sheet(students)