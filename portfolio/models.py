from django.db import models

# Create your models here.
class Project(models.Model):

    def __str__(self):
        return self.proj_name

    proj_name = models.CharField(max_length=200)
    proj_desc = models.CharField(max_length=200)
    proj_img = models.CharField(max_length=500, default='https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Question_Mark.svg/1200px-Question_Mark.svg.png')
