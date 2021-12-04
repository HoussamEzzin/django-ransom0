from django.db import models

# Create your models here.

class Client(models.Model):
    # question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    id = models.AutoField(primary_key=True)
    key =models.TextField(null=False)
    date = models.DateTimeField('Date')
    decrypted = models.TextField()
    