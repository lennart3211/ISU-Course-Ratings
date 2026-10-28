# can expand file to all domain classes

class Department:
    pass

class CourseLevel:
    pass


class Course:
    def __init__(self, course_id: int, title: str, \
                department_code: str, catalog_number: str, \
                level: CourseLevel, description: str, \
                credits: int, average_rating: float, \
                material_links: list, ratings: list):
        self.course_id = course_id
        self.title = title
        self.department_code = department_code
        self.catalog_number = catalog_number
        self.level = level
        self.description = description
        self.credits = credits
        self.average_rating = average_rating
        self.material_links = material_links
        self.ratings = ratings

    def get_average_rating(self) -> float:
        return self.average_rating

    def recalculate_average(self):
        self.average_rating = sum(r.score for r in self.ratings) / len(self.ratings) if self.ratings else 0

