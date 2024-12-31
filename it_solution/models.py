from django.db import models
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError

# Create your models here.
def number_less_than_100(number):
    print(number)
    if number < 0:
        raise ValidationError(
            "Not a valid number"
        )
    elif number > 100:
        raise ValidationError(
            "Not a valid number"
        )
    else:
        return True
    

class LatestNews(models.Model):
    image= models.ImageField(upload_to='latestnews/')
    title= models.CharField(max_length=255)
    admin= models.CharField(max_length=255)
    content= RichTextField()
    date= models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
class Comment(models.Model):
    news = models.ForeignKey(LatestNews, on_delete=models.CASCADE, related_name='news_comments')
    comment= models.TextField()
    name= models.CharField(max_length=100)
    create_on= models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return f"{self.name} |{self.comment[:70]}"

class MeetExports(models.Model):
    name= models.CharField(max_length=255)
    image= models.ImageField(upload_to='meetexports/')
    postition= models.CharField(max_length=255)
    twitter=models.URLField(blank=True, null=True)
    facebook= models.URLField(blank=True, null=True)
    insta= models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Technology(models.Model):
    logo= models.ImageField(upload_to='technology/')


    

class Project(models.Model):
    image= models.ImageField(upload_to='project/')
    title= models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    description=RichTextField()


    def __str__(self):
        return self.title
    



class Services(models.Model):
    image= models.ImageField(upload_to='services/')
    tilte= models.CharField(max_length=100)
    description= models.TextField()
    
    def __str__(self):
        return self.tilte
    

class BusinessGrowth(models.Model):
    image= models.ImageField(upload_to='businessgrowth/')
    tilte= models.CharField(max_length=100)
    short_description= models.TextField()
    long_description= models.TextField()
    sucess=models.IntegerField(validators=[number_less_than_100])
    problem_solved= models.IntegerField(validators=[number_less_than_100])

    def __str__(self):
        return self.tilte
    

    @property
    def percentage_solved(self):
        return self.problem_solved / 100
    
    def suces_percentage(self):
        return self.sucess / 100
    


class CostumerFeedbacks(models.Model):
    name= models.CharField(max_length=255)
    image= models.ImageField(upload_to='costumer_feedbacks/')
    position = models.CharField(max_length=100)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.name)
    



class Message(models.Model):
    name= models.CharField(max_length=255)
    email= models.EmailField()
    message= models.TextField()


    def __str__(self):
        return self.name 
