from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Musician(models.Model):
    id= models.AutoField(primary_key=True)
    f_name=models.CharField(max_length=20)
    l_name=models.CharField(max_length=20)
    instrument= models.CharField(max_length=20)

class Album(models.Model):
    artist=models.ForeignKey(Musician,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    release_date= models.DateField()

class UserProfileInfo(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio= models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_pics',blank = True)

    def __str__(self):
        return self.user.username
