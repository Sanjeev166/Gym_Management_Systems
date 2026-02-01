from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User_A(AbstractUser):
    role_choices = ((1, 'Admin'),
                    (2, 'Member'))
    role = models.IntegerField(default=1, choices=role_choices)
   
class Plans(models.Model):        
    Duration_months = models.CharField(max_length=200, null=True)
    Price = models.FloatField(default=0)
    Session_hrperday = models.CharField(max_length=200, null=True, default='1.5')
    
    def __str__(self):
        return self.Duration_months   
          
class Members(models.Model):
    user = models.CharField(max_length=12, null=True, unique=True)
    Mobile = models.IntegerField(unique=True, default=0)
    Address = models.CharField(max_length=25, null=True)
    Plan = models.ForeignKey(Plans, on_delete=models.SET_NULL, null=True)
    Amount = models.FloatField()    
    
    def __str__(self):
        return self.user
      
class Members_Details(models.Model):
    Member = models.ForeignKey(Members, on_delete=models.CASCADE, null=True)
    start_date = models.DateField(auto_now_add=True)
    
    def _str_(self):
        return self.Member        