from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views
from .controllers import AuthController

authController = AuthController()

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/<slug:courseSlug>/', views.course_page, name='course-page'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('api/register/', authController.register, name='api-register'),
    path('api/login/', authController.login, name='api-login'),
    path('api/logout/', authController.logout, name='api-logout'),
    path('account/edit/', login_required(authController.editAccount), name='edit-account'),
    path('account/delete/', login_required(authController.deleteAccount), name='delete-account'),
]
