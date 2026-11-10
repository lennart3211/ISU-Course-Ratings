from django.views import View

class CourseController:
    def search(self, request):
        pass

    def filter(self, request):
        pass

    def sort(self, request):
        pass

    def coursePage(self, request, courseID):
        pass

    def saveCourse(self, request, courseID):
        pass    

    def savedCourses(self, request):
        pass
    
    def uploadCourse(self, request):
        pass

    def editCourse(self, request, courseID):
        pass    

    def deleteCourse(self, request, courseID):
        pass

    def addMaterialLink(self, request, courseID):
        pass

    def editReview(self, request, reviewID):
        pass

    def createReview(self, request, courseID):
        pass

    def deleteReview(self, request, reviewID):
        pass

    def replyToReview(self, request, reviewID):
        pass

    def deleteReply(self, request, replyID):
        pass

    def voteOnReview(self, request, reviewID):
        pass
