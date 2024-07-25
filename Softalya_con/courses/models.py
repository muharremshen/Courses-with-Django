from django.db import models
from teachers.models import Teacher
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,unique=True,null=True)

    def __str__(self) -> str:
        return  self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,unique=True,null=True)
    
    def __str__(self) -> str:
        return  self.name

class Course(models.Model):
    name = models.CharField(max_length=200, unique=True)
    teacher=models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,null=True ,on_delete=models.DO_NOTHING)
    tags= models.ManyToManyField(Tag,blank=True)
    students=models.ManyToManyField(User, blank=True, related_name="courses_joined")
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to="courses/%y/%m/%d/",default="courses/default_foto.png")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)


    def __str__(self) -> str:
        return  self.name