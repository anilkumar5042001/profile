from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()

class File(models.Model):
    file = models.FileField(blank=False, null=False)
    remark = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

