from django.db import models
from memberships.models import Memberships

# Create your models here.
class Courses(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    allowed_memberships = models.ManyToManyField(Memberships)

    def __str__(self):
        return self.title
    
class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    course = models.ForeignKey(Courses,on_delete=models.SET_NULL,null=True)
    position = models.IntegerField()
    video_url = models.CharField(max_length=200)
    thumbail = models.ImageField(upload_to='thumbail')

    def __str__(self):
        return self.title