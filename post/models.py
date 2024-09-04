from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class PostModel(models.Model):
    name_post = models.CharField(max_length=100)
    txt_post = models.CharField(max_length=10000000)
    date = models.DateTimeField(datetime.now(tz=None))
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Name Post: {self.name_post} | Author: {self.author}'
    
class CommentModel(models.Model):
    comment = models.CharField(max_length=10000)
    post_nexus = models.ForeignKey(PostModel,on_delete=models.CASCADE,null=True)
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
