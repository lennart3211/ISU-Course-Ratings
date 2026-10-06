# can expand file to all domain classes

class Course:
    def __init__(self, course_id, title, department, course_level, description, min_credits, max_credits, course_materials):
        self.course_id = course_id
        self.title = title
        self.department = department
        self.course_level = course_level
        self.description = description
        self.min_credits = min_credits
        self.max_credits = max_credits
        self.course_materials = []