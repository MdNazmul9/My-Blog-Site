from django.db import models
from ckeditor.fields import RichTextField
#from djrichtextfield.models import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
from django.contrib.auth.models import User
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    #body = models.TextField()
    
    body = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title