from User import User
from Course import Course
from Assignment import Assignment
from Student import Student
class Doctor(User):
    def __init__(self, id, username, password, full_name, email):
        super().__init__(id, username, password, full_name, email)
        self.courses = []

    def createCourse(self, name, code):
        # Check if course already exists
        if any(course.code == code for course in self.courses):
            print(f"Course with code {code} already exists.")
            return
        course = Course(name, code, self)
        self.courses.append(course)
        Student.available_courses(course)
        print(f"Course '{name}' with code '{code}' created successfully.")

    def listCourses(self):
        if not self.courses:
            print("No courses available.")
        else:
            for course in self.courses:
                print(f"Course Code: {course.code}, Course Name: {course.name}")

    def viewCourse(self, courseCode):
        for course in self.courses:
            if course.code == courseCode:
                return course
        return None

    def mainMenu(self):
        while True:
            print("\nDoctor Main Menu:")
            print("1. List Courses")
            print("2. Create Course")
            print("3. View Course")
            print("4. Log out")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.listCourses()
            elif choice == '2':
                name = input("Enter course name: ")
                code = input("Enter course code: ")
                self.createCourse(name, code)
            elif choice == '3':
                courseCode = input("Enter course code: ")
                course = self.viewCourse(courseCode)
                if course:
                    self.courseMenu(course)
                else:
                    print("Course not found.")
            elif choice == '4':
                return self.signOut()
            else:
                print("Invalid choice. Please try again.")

    def courseMenu(self, course):
        while True:
            print("\nCourse Menu:")
            print("1. List Assignments")
            print("2. Create Assignment")
            print("3. View Assignment")
            print("4. Back")
            choice = input("Enter your choice: ")
            if choice == '1':
                if not course.assignments:
                    print("No assignments available for this course.")
                else:
                    for assignment in course.assignments:
                        print(f"Assignment ID: {assignment.id}, Title: {assignment.title}")
            elif choice == '2':
                title = input("Enter assignment title: ")
                description = input("Enter assignment description: ")
                dueDate = input("Enter due date: ")
                assignment = Assignment(len(course.assignments) + 1, title, description, dueDate, course)
                course.addAssignment(assignment)
                print(f"Assignment '{title}' created successfully.")
            elif choice == '3':
                assignmentId = int(input("Enter assignment ID: "))
                assignment = course.viewAssignment(assignmentId)
                if assignment:
                    self.assignmentMenu(assignment)
                else:
                    print("Assignment not found.")
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def assignmentMenu(self, assignment):
        while True:
            print("\nAssignment Menu:")
            print("1. Show Info")
            print("2. Show Grades Report")
            print("3. List Solutions")
            print("4. View Solution")
            print("5. Back")
            choice = input("Enter your choice: ")
            if choice == '1':
                print(assignment.showInfo())
            elif choice == '2':
                print(assignment.showGradesReport())
            elif choice == '3':
                if not assignment.solutions:
                    print("No solutions available for this assignment.")
                else:
                    for solution in assignment.solutions:
                        print(f"Solution ID: {solution.id}, Student: {solution.student.username}")
            elif choice == '4':
                solutionId = int(input("Enter solution ID: "))
                solution = assignment.viewSolution(solutionId)
                if solution:
                    print(solution.showInfo())
                else:
                    print("Solution not found.")
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")
