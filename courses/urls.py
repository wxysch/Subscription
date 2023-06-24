from django.urls import path
from .views import CourseListView,CoursesDetailView,LessonDetailView
app_name='courses'

urlpatterns = [
    path('',CourseListView.as_view(),name='list'),
    path('<slug>',CoursesDetailView.as_view(),name='detail'),
    path('<course_slug>/<lesson_slug>',LessonDetailView.as_view(),name='lesson_detail')
]