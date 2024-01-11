class Student:
    
    count = 0
    
    def __init__(self):
        self.name = input("Enter Student Name: ")
        self.age = int(input("Enter Student Age: "))
        self.department = input("Enter Student Department (PGDM(p)/B.Tech(b)): ").capitalize()
        
        Student.count += 1

    def display(self):
        print("Name:", self.name, "Age:", self.age, "Department:", self.department)

print("""------ STUDENT ADMIT ------""")

pgdm_students = []
btech_students = []

num_students = int(input("Enter The Total Number Of Students: "))

for _ in range(num_students):
    new_student = Student()
    new_student.display()
    
    if new_student.department == 'P':
        pgdm_students.append(new_student)
    
    elif new_student.department == 'B':
        btech_students.append(new_student)

print("*****************")

print("\nTotal PGDM Department Students:")
for student in pgdm_students:
    student.display()

print("\nTotal B.Tech Department Students:")
for student in btech_students:
    student.display()

print("\nTotal Number Of students:", Student.count)