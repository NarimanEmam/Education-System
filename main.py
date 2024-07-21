from Student import Student
from Doctor import Doctor
from Course import Course
from Assignment import Assignment
from AssignmentSolution import AssignmentSolution

students = []
doctors = []
courses = []

def add_sample_data():
    doctor1 = Doctor(1, "ali", "password123", "Ali Ahmed", "ali@example.com")
    doctor2 = Doctor(2, "sara", "password123", "Sara Mohamed", "sara@example.com")
    doctors.extend([doctor1, doctor2])
    
    course1 = Course("Introduction to Programming", "PROG101", doctor1)
    course2 = Course("Data Structures", "DS202", doctor2)
    courses.extend([course1, course2])

    student1 = Student(1, "john_doe", "password123", "John Doe", "john@example.com")
    student2 = Student(2, "jane_doe", "password123", "Jane Doe", "jane@example.com")
    students.extend([student1, student2])



    student1.registerCourse(course1)
    student2.registerCourse(course2)
    
    assignment1 = Assignment(1, "Assignment 1: Basics of Programming", "Complete the basic programming exercises.", "2024-08-15", course1)
    assignment2 = Assignment(2, "Assignment 2: Advanced Data Structures", "Solve problems related to advanced data structures.", "2024-09-01", course2)
    course1.addAssignment(assignment1)
    course2.addAssignment(assignment2)


    solution1 = AssignmentSolution(1, student1, assignment1, "My solution to the basics of programming assignment.")
    solution2 = AssignmentSolution(2, student2, assignment2, "My solution to the advanced data structures assignment.")
    assignment1.solutions.append(solution1)
    assignment2.solutions.append(solution2)

    Student.available_courses(course1)
    Student.available_courses(course1)

def sign_up():
    print("1. Sign up as Student")
    print("2. Sign up as Doctor")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")
        full_name = input("Enter full name: ")
        email = input("Enter email: ")
        
        if any(student.username == username for student in students):
            print("Username already exists.")
            return
        
        student_id = len(students) + 1
        new_student = Student(student_id, username, password, full_name, email)
        students.append(new_student)
        print(f"Student {full_name} registered successfully.")
    
    elif choice == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        full_name = input("Enter full name: ")
        email = input("Enter email: ")
        
        if any(doctor.username == username for doctor in doctors):
            print("Username already exists.")
            return
        
        doctor_id = len(doctors) + 1
        new_doctor = Doctor(doctor_id, username, password, full_name, email)
        doctors.append(new_doctor)
        print(f"Doctor {full_name} registered successfully.")
    
    else:
        print("Invalid choice. Returning to main menu.")

def main():
    add_sample_data()  # Adding sample data

    while True:
        print("\nPlease make a choice:")
        print("1. Login")
        print("2. Sign up")
        print("3. Shutdown system")
        choice = input("Enter your choice: ")
        if choice == '1':
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")
            user = None
            for student in students:
                if student.username == username and student.password == password:
                    user = student
                    break
            if not user:
                for doctor in doctors:
                    if doctor.username == username and doctor.password == password:
                        user = doctor
                        break
            if user:
                print(f"Welcome {user.full_name}. You are logged in.")
                if isinstance(user, Student):
                    user.mainMenu()
                elif isinstance(user, Doctor):
                    user.mainMenu()
            else:
                print("Invalid username or password.")
        elif choice == '2':
            sign_up()
        elif choice == '3':
            print("System is shutting down...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()