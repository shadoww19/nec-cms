from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    collegeId = models.CharField(db_column='College Id', max_length = 20, null=False)
    name = models.CharField(db_column='Name', max_length = 500, null=False)
    email = models.CharField(db_column='Email', max_length = 500, null=False)
    password = models.CharField(db_column='Password', max_length = 1000, null=False)
    role = models.CharField(db_column='Role', max_length = 50, null=False)
    isLoggedIn = models.IntegerField(db_column='Login Status', default=0)
    
class Marks(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    subject1 = models.IntegerField(db_column='Subject 1',null=False)
    subject2 = models.IntegerField(db_column='Subject 2',null=False)
    subject3 = models.IntegerField(db_column='Subject 3',null=False)
    student = models.ForeignKey(User,on_delete=models.CASCADE)