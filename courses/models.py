from django.db import models
from memberships.models import Memberships

from django.urls import reverse

# Create your models here.
class Courses(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    allowed_memberships = models.ManyToManyField(Memberships)

    def __str__(self):
        return self.title   

    def get_absolute_url(self):
        return reverse('courses:detail',kwargs={'slug':self.slug})
    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')

class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    course = models.ForeignKey(Courses,on_delete=models.SET_NULL,null=True)
    position = models.IntegerField()
    video_url = models.CharField(max_length=200)
    thumbail = models.ImageField(upload_to='thumbail')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course:lesson-deatails',
            kwargs={
                'course_slug':self.course.slug,
                'lesson_slug':self.slug
            })