from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=35, unique=True)
    def __str__(self):
        return self.name
    
class Blog (models.Model):

    STATUS = (
        ('d', "Draft"),
        ('p', "Published")
    )

    title = models.CharField(max_length=10, unique=True)
    content = models.TextField(blank=True)
    image = models.ImageField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blog')
    publish_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=5, choices=STATUS, default='d', blank=True)

    
    def __str__(self):
        return f"{self.title} - {self.status} "
    
class Comment (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_post_comment')
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=150, blank=True, null=True) 
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    
class PostViews(models.Model):
    post_views = models.BooleanField(default=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="post_views")
    time_stamp = models.DateField(auto_created=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_post_views")
    
    def __str__(self):
        return f'{self.blog}nu-{self.user} görüntüledi'
    
    
class Likes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name= 'user_likes')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name= 'likes_n')
    likes = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.likes}'
    

    
