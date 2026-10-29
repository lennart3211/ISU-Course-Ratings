from MaterialType import MaterialType

class CourseMaterialLink:
    def __init__(self, link_id, course_id, url, title, type: MaterialType):
        self.link_id = link_id
        self.course_id = course_id
        self.url = url
        self.title = title
        self.type = type

    # def validateURL(self) -> bool:
    # # Basic validation logic (e.g., checking if it starts with http/https)
    #     return self.url.startswith(("http://", "https://"))