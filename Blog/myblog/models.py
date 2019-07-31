from django.db import models
from django.utils import timezone

# Create your models hereself.
class category(models.Model):
    bcategory=models.CharField(max_length=55,default="",editable=True )
    def __str__(self):
        return self.bcategory
class auther(models.Model):
    bauthor=models.CharField(max_length=55,default="", editable=True)
    email = models.CharField(max_length=250, default="", editable=True)
class myblog(models.Model):
    author=models.ForeignKey(auther, on_delete=models.CASCADE)
    btitle=models.CharField(max_length=55,default="", editable=True)
    bdate=models.DateTimeField(default= timezone.now(), null=True, blank=True)
    bdiscription=models.TextField(blank=True, null=True)
    bimage = models.ImageField(upload_to='static/images')

class categoryblog(models.Model):
    cid = models.ForeignKey(category, on_delete=models.CASCADE)
    bid = models.ForeignKey(myblog , on_delete=models.CASCADE)
class comments(models.Model):
    bid = models.ForeignKey(myblog, on_delete=models.CASCADE)
    bcomment = models.CharField(max_length = 10000 , default="" , editable=True)
