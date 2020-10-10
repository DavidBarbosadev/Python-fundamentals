#variables that will be used in the program howerver because the program at this stage did not run, the
#variable are still empty or with 0 because the user did not introduce the data yet.
grade_sum = 0
grade_mean = 0
best_grade = 0
best_grade_student = ""
worst_grade = 0
worst_student_name = ""
student_grades = []
student_names = []



#This function is used to store 4 print statements.
# 2 of those print statements will print 2 list, 1 of them will print the mean.
#The last one will print the best grade, the worst grade, the student that took the best  grade
#And the student who took the worst grade.
def student_grades_names_list():
    print(student_names)
    print(student_grades)
    #The use of the :.3f is to allow the program to print the mean with 3 float cases.
    print(f"\n\tThe grade's mean was {grade_mean:.3f} %")
    print(f"\n\n The best grade was {best_grade} %\n and the name of the student who"
          f" got that grade was {best_grade_student}\n and the worst "
          f" grade was {worst_grade} % and the student who got that grade "
          f"was {worst_student_name}. ")


#This function stores the if statement of the grades.
#For example the user says that the first student took 20 % on the exam.
#This print statement after receive that information will print "The student got negative on the exam".
#This format of the print statement is the new format of print in python 3.6 .
def grade_results():
    if grade <= 49.9:
        print("The student got negative on the exam")
    elif grade <= 69.9:
        print("The student got a positive grade and it was good!")
    elif grade <= 89.9:
        print("The student got a positive grade and it was a very good grade!")
    elif grade <= 99.9:
        print("The student got a positive grade and got a excellent grade!")
    elif grade == 100:
        print(" the student got everything right on the exam and got the perfect grade!")
    else:
        print("The grades just go between 0 and 100 ")
#These print statements are used in order to create a better look on the program.
print("************************")
print("\tStudent's Grades")
print("************************\n")
#This for loop was used in order to receive the information of 5 different students.
# The user should introduce the gender, the name, the age and the grade in order to get more content,
#in the program so the program gets more complete and improved.
for s in range (1,6):
    print(f"----{s}º student ----")
    gender = str(input("Gender [M/F]:  ")).strip().upper()[0]
    #The while loops were used in order to let the user reintroduce the data in case the user missed,
    #the type of data that the program was looking for .
    # The gender while loop was used in order to improve the program. Because this loop only allow the user,
    # to write the letters M, m (male) or F, f (female).
    # The .strip().upper[0], makes the program only read the first letter that the user introduced and this
    #  improved the program as well.
    while gender not in "MmFm":
        gender = str(input("Invalid data. Please inform the gender of the student: ")).strip().upper()[0]
    name = str(input("Name: "))
    while True:
        try:
            age = int(input("Age: "))
            break
        except ValueError:
            print("Invalid data. Please inform the age of the student" )
    while True:
        try:
            grade = float(input("Grade: "))
            break
        except ValueError:
            print("Invalid data. Please inform the grade of the student" )
    grade_sum += grade
    #If statement used in order to find the best grade, the best grade student, the worst grad and the worst
    #grade student.
    if s == 1 and gender in "MmFf":
        best_grade = grade
        best_grade_student = name
    if gender in "MmFf" and grade > best_grade:
        best_grade = grade
        best_grade_student = name
    if s == 1 and gender in "MmFf":
        worst_grade = grade
        worst_student_name = name
    if gender in "MmFf" and grade < worst_grade:
        worst_grade = grade
        worst_student_name = name
    #This grade_results will execute the function above. The one related to the students classifications
    grade_results()
    #Used the .append in order to store the values of the varieble grade inside the list student_grades
    student_grades.append(grade)
    #Used the .append in order to store the values of the varieble name inside the list student_names.
    student_names.append(name)
    #used the .sort with the reverse=true in order to store the values in a decreasing position and to print
    #them later in that position as well.
    student_grades.sort(reverse=True)
#print statement was used in order to create a gap between the the list of students and the grade's mean.
print("\n\n")
#Mean calculation
grade_mean = grade_sum / 5
#This function will execute the function above. The one related to the lists.
student_grades_names_list()









