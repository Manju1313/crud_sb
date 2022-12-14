from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.CharField(max_length=25)
    ename=models.CharField(max_length=25)
    eemail=models.EmailField()
    econtact=models.CharField(max_length=25)

    def __str__(self):
        return "%s" %(self.ename)


    class Meta:
        db_table="emp"
