from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Post(models.Model):
    id = models.UUIDField(max_length=100, editable=False, primary_key=True, unique=True, default=uuid.uuid4)
    title = models.CharField(max_length=500)
    artist = models.CharField(max_length=500, null=True)
    url = models.URLField(max_length=500, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')
    image = models.URLField(max_length=500)
    body = models.TextField()
    tags = models.ManyToManyField('Tag')
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return str(self.title)
    
    
class Tag(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)
    image = models.FileField(upload_to='icons/', null=True, blank=True)
    order = models.IntegerField(null=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return str(self.name)
    
    
class Comment(models.Model):
    id = models.CharField(max_length=100, default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        try:
            return f"{self.author.username}: {self.body[:30]}"
        except:
            return f"No Name: {self.body[:30]}"
    
    
    
    
    