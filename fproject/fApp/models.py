from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))
    title = models.CharField(max_length=264)
    slug = models.SlugField(max_length=264, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    likes = models.ManyToManyField(User,related_name='blog_post',blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='blog_comments',on_delete=models.CASCADE,null=True,blank=True)
    reply = models.ForeignKey('Comment',null=True,related_name='replies',on_delete=models.CASCADE)
    name = models.CharField(max_length=20,blank=True)
    body = models.CharField(max_length=15,blank=True)
    date_added = models.DateTimeField(default=timezone.now,null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
