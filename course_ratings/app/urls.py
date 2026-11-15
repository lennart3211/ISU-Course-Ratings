from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/<slug:courseSlug>/', views.course_page, name='course-page'),
]
