from User import User
from AssignmentSolution import AssignmentSolution
from Course import Course
class Student(User):

    courses = []
    def __init__(self, id, username, password, full_name, email):
        super().__init__(id, username, password, full_name, email)
        self.registeredCourses = []

    @staticmethod
    def available_courses(course):
        Student.courses.append(course)
    def registerCourse(self, course):
        self.registeredCourses.append(course)
        course.students.append(self)

    def listMyCourses(self):
        return self.registeredCourses

    def viewCourse(self, courseCode):
        for course in self.registeredCourses:
            if course.code == courseCode:
                return course
        return None

    def submitAssignment(self, courseCode, assignmentId, solution):
        course = self.viewCourse(courseCode)
        if course:
            for assignment in course.assignments:
                if assignment.id == assignmentId:
                    assignmentSolution = AssignmentSolution(len(assignment.solutions) + 1, self, assignment, solution)
                    assignment.solutions.append(assignmentSolution)

    def viewGrades(self):
        grades = {}
        for course in self.registeredCourses:
            courseGrades = {assignment.id: None for assignment in course.assignments}
            for assignment in course.assignments:
                for solution in assignment.solutions:
                    if solution.student == self:
                        courseGrades[assignment.id] = solution.grade
            grades[course.code] = courseGrades
        return grades

    def mainMenu(self):
        global courses
        while True:
            print("\nStudent Main Menu:")
            print("1. Register in Course")
            print("2. List My Courses")
            print("3. View Course")
            print("4. Grades Report")
            print("5. Log out")
            choice = input("Enter your choice: ")
            if choice == '1':
                for course in Student.courses:
                    if course not in self.registeredCourses:
                        print(f"{course.code}: {course.name}")
                courseCode = input("Enter course code to register: ")
                for course in Student.courses:
                    if course.code == courseCode and course not in self.registeredCourses:
                        self.registerCourse(course)
                        print(f"Registered in course {course.name}")
                        break
                else:
                    print("Invalid course code or already registered.")
            elif choice == '2':
                for course in self.registeredCourses:
                    print(f"{course.code}: {course.name}")
            elif choice == '3':
                courseCode = input("Enter course code: ")
                course = self.viewCourse(courseCode)
                if course:
                    print(f"{course.name} ({course.code})")
                    for assignment in course.assignments:
                        print(f"Assignment {assignment.id}: {assignment.title}")
            elif choice == '4':
                grades = self.viewGrades()
                for courseCode, courseGrades in grades.items():
                    print(f"Course {courseCode}:")
                    for assignmentId, grade in courseGrades.items():
                        print(f"Assignment {assignmentId}: Grade {grade}")
            elif choice == '5':
                return self.signOut()
            else:
                print("Invalid choice. Please try again.")
