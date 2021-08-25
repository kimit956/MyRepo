
#Class name
def className():
    try:
        className = input("What would you like to call this class? ")
    except ValueError:
        className = input("Invalid name. Enter a different name for the class: ")


#Asks for student names and adds to array
def studentNames(students,numStudents):
    name = ""
        
    #will ask user for student names x amount of times
    for x in range(numStudents):
        try:
            name = input("Enter student's name: ")
        except ValueError:
            name = input("Please enter a valid student name: ")
        students.append(name)


#Asks for grades and adds to array
def studentGrades(grades,numStudents):
    singleGrade = ""
    
    #asks the user for grades
    for y in range(numStudents):
        try:
            singleGrade = input("Enter student's grade: ")
        except ValueError:
            singleGrade = input("Enter a valid letter for the student's grade: ")
            
        singleGrade = singleGrade.capitalize()
        #Checks that the entered grade is valid
        while (singleGrade != "A" and singleGrade != "B" and singleGrade != "C" and singleGrade != "D" and singleGrade != "F"):
            singleGrade = input("Please enter a valid letter for the student's grade: ")
        
        #adds the corrected grade letter to the array
        grades.append(singleGrade)


#Converts letters to numbers to do average
def gradeConverter(grades,numStudents):
    totals = 0
    
    #iterates through each element in grades array
    for j, element in enumerate(grades):
        if (grades[j] == "a" or grades[j] == "A"):
            grades[j] = int(4)
        elif (grades[j] == "b" or grades[j] == "B"):
            grades[j] = int(3)
        elif (grades[j] == "c" or grades[j] == "C"):
            grades[j] = int(2)
        elif (grades[j] == "d" or grades[j] == "D"):
            grades[j] = int(1)
        elif (grades[j] == "f" or grades[j] == "F"):
            grades[j] = int(0)
        totals += grades[j]
    
    #This is just grammar
    if numStudents == 1:
        print("\nIn a class of " + str(numStudents) + " student, the class average will be " + str(totals/len(grades)))
    else:
        print("\nIn a class of " + str(numStudents) + " students, the class average will be " + str(totals/len(grades)))
        

def printInfo(students,grades):    
    print("          Name              Grade          ")
    print("===========================================")
    for k, element in enumerate(students):
        print("         ",students[k],end='')
        print(" " * (19 - len(students[k])),grades[k]) #This gets the grade lined up correctly


#Student names: Will ask user for however many students there are
def main():
    print("*******************************************")
    
    keepAsking = ""
    while keepAsking != "N" or keepAsking != "n":
        students = []
        grades = []
        
        className()
        
        #asks the user how many students will be entered and allows only numbers
        try:
            numStudents = int(input("How many student(s) will you be entering grades for? "))
        except ValueError:
            numStudents = int(input("Please enter a number value: "))
        
        #Calls the functions
        studentNames(students,numStudents)
        studentGrades(grades,numStudents)
        printInfo(students,grades)
        gradeConverter(grades,numStudents)
        
        #asks the user if he/she would like to do another class
        try:
            keepAsking = input("\nWould you like to do another class (y/n)? ")
        except ValueError:
            keepAsking = input("Yes or No (y\n): ")
            
        if keepAsking == "n" or keepAsking == "N":
            print("Goodbye!")
            break
        
        print("*******************************************\n")
    
main()
