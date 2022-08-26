from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime,date

class category(models.Model):
     name=models.CharField(max_length=255)
     def __str__(self):
        return self.name

     def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title=models.CharField(max_length=255)
    title_tag=models.CharField(max_length=255)#default="blog hub")
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()  
    post_date= models.DateField(auto_now_add=True)
    category=models.CharField(max_length=255)#default="")
    likes=models.ManyToManyField(User,related_name='blog_posts')


    def __str__(self):
        return self.title+ ' | '+str(self.author)

    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.id)))
    


























