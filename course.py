# can expand file to all domain classes

class Department:
    pass

class CourseLevel:
    pass

class Course:
    def __init__(self, course_id: int, title: str, department: Department, course_level: CourseLevel, description: str, min_credits: int, max_credits: int, course_materials: list):
        self.course_id = course_id
        self.title = title
        self.department = department
        self.course_level = course_level
        self.description = description
        self.min_credits = min_credits
        self.max_credits = max_credits
        self.course_materials = []

