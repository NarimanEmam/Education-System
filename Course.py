class Course:
    def __init__(self, name, code, doctor):
        self.name = name
        self.code = code
        self.doctor = doctor
        self.teachingAssistants = []
        self.students = []
        self.assignments = []

    def addAssignment(self, assignment):
        self.assignments.append(assignment)

    def listAssignments(self):
        return self.assignments

    def viewAssignment(self, assignmentId):
        for assignment in self.assignments:
            if assignment.id == assignmentId:
                return assignment
        return None
