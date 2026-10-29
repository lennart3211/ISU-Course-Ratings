from DBConnection import DBConnection
from course import Course
from CourseMaterialLink import CourseMaterialLink
from typing import List, Optional

class CourseStorage:

  def __init__(self, db: DBConnection):
    self.db = db

  def saveCourse(self, course: Course) -> None:
    pass

  def retreiveCourse(self, courseID: int) -> Optional[Course]:
    return None

  def retreiveCoursesByName(self, name: str) -> List[Course]:
    return []

  def retreiveCoursesByDepartment(self, departmentCode: str) -> List[Course]:
    return []

  def deleteCourse(self, courseID: int) -> None:
    pass

  def saveMaterialLink(self, link: CourseMaterialLink) -> None:
    pass

  def saveSavedCourse(self, userID: int, courseID: int) -> None:
    pass

  def retreiveSavedCourses(self, userID: int) -> List[Course]:
    return []