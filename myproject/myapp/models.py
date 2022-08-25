from django.db import models

 
# Create your models here.
class StudentForm(models.Model):  
    
    file  = models.FileField() 
   
    class Meta:  
        db_table = "data"