from django.shortcuts import render

from app.controllers import CourseController

courseController = CourseController()


def home(request):
    return render(request, 'app/home.html')


def course_page(request, courseSlug):
    # TODO: resolve courseSlug -> courseID via CourseHandler/CourseService
    # once the Course model exists, then delegate to
    # courseController.coursePage(request, courseID) per the diagram's
    # int-based coursePage(request, courseID) signature.
    return render(request, 'app/course_page.html', {'courseSlug': courseSlug})
