from typing import List, Optional
from course import Course
from User import User
from Admin import Admin
from CourseMaterialLink import CourseMaterialLink

class CourseHandler():

  def __init__(self, course_storage: CourseStorage):
    super().__init__()
    self.course_storage = course_storage

  def searchByName(self, name: str) -> List[Course]:
    return self.course_storage.retreiveCoursesByName(name)

  def filterByDepartment(self, departmentCode: str) -> List[Course]:
    return self.course_storage.retreiveCoursesByDepartment(departmentCode)

  def sortByRating(self, ascending: bool) -> List[Course]:
    courses = self.course_storage.retreiveCoursesByName("")  # Example retrieval
    return sorted(courses, key=lambda c: c.averageRating, reverse=not ascending)

  def getCoursePage(self, courseID: int) -> Optional[Course]:
    return self.course_storage.retreiveCourse(courseID)

  def saveCourse(self, user: User, course: Course) -> None:
    self.course_storage.saveSavedCourse(user.userID, course.courseID)

  def getSavedCourses(self, user: User) -> List[Course]:
    return self.course_storage.retreiveSavedCourses(user.userID)

  def uploadCourse(self, admin: Admin, course: Course) -> None:
    self.course_storage.saveCourse(course)

  def editCourse(self, admin: Admin, course: Course) -> None:
    self.course_storage.saveCourse(course)

  def deleteCourse(self, courseID: int) -> None:
    self.course_storage.deleteCourse(courseID)

  def addMaterialLink(
      self, admin: Admin, course: Course, link: CourseMaterialLink
  ) -> None:
    self.course_storage.saveMaterialLink(link)