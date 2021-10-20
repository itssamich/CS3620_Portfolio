from django.db import models

# Create your models here.
class ContactMsg(models.Model):
    def __str__(self):
        return self.hobby_name

    msg_author = models.CharField(max_length=200)
    msg_email = models.EmailField(max_length=200)
    msg_message = models.TextField(max_length=600)