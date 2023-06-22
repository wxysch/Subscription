from django.shortcuts import render

from .models import Courses

from django.views.generic import ListView,DetailView
# Create your views here.
class CourseListView(ListView):
    model = Courses

class CoursesDetailView(DetailView):
    model = Courses