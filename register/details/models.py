from django.db import models

# Create your models here.
class student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    def __str__(self):
        return self.name
