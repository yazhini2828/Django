from django.db import models

class Members(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  age = models.IntegerField(blank=True, null=True)
  mobile_no = models.IntegerField(blank=True, null=True)
  email_id = models.EmailField(max_length=236,default='some string')
  location = models.CharField(max_length=255,default='')
  total_marks_scored = models.IntegerField(blank=True, null=True)
  Preferred_course=models.CharField(max_length=255,default='SOME STRING')
