from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
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


class AuthController:
    def login(self, request):
        user = authenticate(username=request.POST.get("username"),\
                            password=request.POST.get("password"))
        if user is None:
            messages.error(request, "Invalid")
            return redirect("login")
        auth_login(request, user)
        messages.success(request, "Logged in")
        return redirect("home")

    def logout(self, request):
        auth_logout(request)
        messages.info(request, "Logged out")
        return redirect("home")

    def register(self, request):
        User.objects.create_user(username=request.POST.get("username"),\
                                 email=request.POST.get("email"),\
                                 password=request.POST.get("password"))
        messages.success(request, "Registered")
        return redirect("login")

    def editAccount(self, request):
        request.user.username = request.POST.get("username")
        request.user.email = request.POST.get("email")
        request.user.save()
        messages.success(request, "Updated")
        return redirect("home")

    def deleteAccount(self, request):
        request.user.delete()
        messages.info(request, "Account deleted")
        return redirect("home")