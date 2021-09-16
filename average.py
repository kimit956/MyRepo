def student(student_Name, grade):
    q = "y"
    while q == "y" or q == "":
        student_Name.append(input("What is the student's name? "))
        single_grade = input("What is the student's grade for the class? ").lower()

        while single_grade != "a" and single_grade != "b" and single_grade != "c" and single_grade != "d" and single_grade != "f":
            single_grade = input("Enter a valid letter grade for this student: ")

        grade.append(single_grade)
        q = input("Would you like to add another student (Y|N)? ").lower()
        print()


def converter(grade, values):
    totals = 0

    for i, element in enumerate(grade):
        if grade[i] == "a":
            values.append(4.0)
        elif grade[i] == "b":
            values.append(3.0)
        elif grade[i] == "c":
            values.append(2.0)
        elif grade[i] == "d":
            values.append(1.0)
        elif grade[i] == "f":
            values.append(0.0)

    totals = sum(values) / len(values)
    print("Class average is: " + str(totals))


# print class average
student_Name = []
grade = []
values = []

student(student_Name,grade)

# zips together both arrays
for i, j in zip(student_Name,grade):
    print(f"{i} has a(n) {j} in the class\n")

converter(grade,values)



