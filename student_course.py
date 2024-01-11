#Multiple Inheritance

class LetsUpgrade:
    lu_courses=[{'Subject': 'Maths', 'Trainer': 'Saikiran', 'Duration': 100},
                {'Subject': 'Python', 'Trainer': 'Saikiran', 'Duration': 150},
                {'Subject': 'Web design', 'Trainer': 'Prasad', 'Duration': 130}]

class ITM:
    itm_courses=[{'Subject': 'Maths', 'Trainer': 'Sheetal', 'Duration': 90},
                {'Subject': 'DSA', 'Trainer': 'Sumit', 'Duration': 200},
                {'Subject': 'Computer Fundamentals', 'Trainer': 'Sumit', 'Duration': 150}]

class CourseSelector(LetsUpgrade, ITM):
    def print_subjects(self, selected_class):
        if selected_class == 'LetsUpgrade':
            subjects = [course['Subject'] for course in self.lu_courses]
        elif selected_class == 'ITM':
            subjects = [course['Subject'] for course in self.itm_courses]
        else:
            subjects = []

        if not subjects:
            print(f"No subjects available for {selected_class}")
            return

        print(f"Available subjects for {selected_class}: {subjects}")

        selected_subject = input("Enter the subject you want details for: ")

        if selected_subject in subjects:
            if selected_class == 'LetsUpgrade':
                selected_course = next(course for course in self.lu_courses if course['Subject'] == selected_subject)
            elif selected_class == 'ITM':
                selected_course = next(course for course in self.itm_courses if course['Subject'] == selected_subject)

            print(f"\nDetails of {selected_subject} in {selected_class}:")
            print(f"Trainer: {selected_course['Trainer']} sir")
            print(f"Duration: {selected_course['Duration']} hours")
        else:
            print(selected_subject, " is not available in ", selected_class)

        enroll_option = input("\nDo you wish to enroll? (yes/no): ").lower()
            
        if enroll_option == 'yes':
            name = input("Enter your Name: ")
            dob = input("Enter you DOB (DD/MM/YYYY): ")
            age = int(input("Enter your Age: "))
            marks = int(input("Enter your 12th Marks: "))
            location = input("Enter your Location: ")
        
            if marks >= 60:
                print("\nCongratulations! You are enrolled in ", selected_subject)
                print("\n----- Student Details -----")
                print("Name: ", name)
                print("Age: ", age)
                print("Date Of Birth: ", dob)
                print("12th Marks: ", marks, "%")
                print("Location: ", location)
            else:
                print("\nSorry! You are not eligible for this course.")

        else:
            print(selected_subject, " is not available in ", selected_class)

course_selector = CourseSelector()

selected_class = input("Enter the class (LetsUpgrade or ITM): ")
course_selector.print_subjects(selected_class)


