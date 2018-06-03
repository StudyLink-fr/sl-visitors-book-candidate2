from django.db import models


class Notice(models.Model):
    notice_title = models.CharField(max_length=100)
    notice_text = models.CharField(max_length=500)
    post_pseudo = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.notice_title

class User(models.Model):
    pseudo = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.pseudo

# Create your models here.
