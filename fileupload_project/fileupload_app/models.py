from django.db import models

# Create your models here.
class Document(models.Model):
    docfile=models.FileField(upload_to='documents')

class Teacher(models.Model):
	first_name=models.CharField(max_length=20)
	last_name=models.CharField(max_length=20)
	middle_name=models.CharField(max_length=20)
	
	def __str__(self):
		return '%s %s %s' % (self.first_name,self.middle_name,self.last_name)

