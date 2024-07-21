class Assignment:
    def __init__(self, id, title, description, dueDate, course):
        self.id = id
        self.title = title
        self.description = description
        self.dueDate = dueDate
        self.course = course
        self.solutions = []

    def showInfo(self):
        return f"Title: {self.title}, Description: {self.description}, Due Date: {self.dueDate}"

    def showGradesReport(self):
        report = {}
        for solution in self.solutions:
            report[solution.student.username] = solution.grade
        return report

    def listSolutions(self):
        return self.solutions

    def viewSolution(self, solutionId):
        for solution in self.solutions:
            if solution.id == solutionId:
                return solution
        return None
