first_name = input("Enter the first student's name: ")
first_id = int(input("Enter the first student's ID: "))
first_grade = float(input("Enter the first student's grade: "))

second_name = input("Enter the second student's name: ")
second_id = int(input("Enter the second student's ID: "))
second_grade = float(input("Enter the second student's grade: "))

print('\n\nInformat for students and their "Math" grades')
print(first_name,'(ID' , str(first_id)+')' , "got grade:" , first_grade)
print(second_name,'(ID' , str(second_id)+')' , "got grade:" , second_grade)
print("Average math grade is" , (first_grade+second_grade)/2 )