from django.urls import path
from .views import CourseListView,CoursesDetailView
app_name='courses'

urlpatterns = [
    path('',CourseListView.as_view(),name='list'),
    path('<slug>',CoursesDetailView.as_view(),name='detail'),
]