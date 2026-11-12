from django.views import View

from app.handlers import AuthHandler


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


class AuthController:
    def __init__(self, authHandler=None):
        self.authHandler = authHandler or AuthHandler()

    def login(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        entity = self.authHandler.login(username, password)

    def logout(self, request):
        entity = request.user
        self.authHandler.logout(entity)

    def register(self, request):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = self.authHandler.registerUser(username, email, password)

    def editAccount(self, request):
        user = request.user
        username = request.POST.get("username")
        email = request.POST.get("email")
        self.authHandler.editAccount(user, username, email)

    def deleteAccount(self, request):
        user = request.user
        self.authHandler.deleteAccount(user)
