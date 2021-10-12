from django.db import models

# Create your models here.
class Hobby(models.Model):

    def __str__(self):
        return self.hobby_name

    hobby_name = models.CharField(max_length=200)
    hobby_desc = models.CharField(max_length=300)
    hobby_img = models.CharField(max_length=500, default = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Question_Mark.svg/1200px-Question_Mark.svg.png')

    

