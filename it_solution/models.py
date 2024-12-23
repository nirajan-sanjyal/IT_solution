from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class LatetNews(models.Model):
    image= models.ImageField()
    title= models.CharField(max_length=255)
    admin= models.CharField(max_length=255)
    content= RichTextField()
    comment= models.CharField()
    date= models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    

class ExploreProjects(models.Model):
    name= models.CharField()
    image= models.ImageField()
    postition= models.CharField()
    twitter=models.URLField()
    facebook= models.URLField()
    insta= models.URLField()

    def __str__(self):
        return self.name
    
class Technology(models.Model):
    logo= models.ImageField()

    def __str__(self):
        return self.logo
    

class Project(models.Model):
    image= models.ImageField()
    title= models.CharField()
    category=models.CharField()
    description=RichTextField()


    def __str__(self):
        return self.title
    

class BusinessGrowth(models.Model):
    image= models.ImageField()
    tilte= models.CharField(max_length=50)
    short_description= models.TextField()
    long_description= models.TextField()
    sucess=models.BigIntegerField()
    problem_solved= models.BigIntegerField()

    def __str__(self):
        return self.tilte