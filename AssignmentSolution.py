class AssignmentSolution:
    def __init__(self, id, student, assignment, solution):
        self.id = id
        self.student = student
        self.assignment = assignment
        self.solution = solution
        self.grade = None
        self.comment = None

    def showInfo(self):
        return f"Solution: {self.solution}, Grade: {self.grade}, Comment: {self.comment}"
