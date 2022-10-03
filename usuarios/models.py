from django.db import models

# Create your models here.
class User(models.Model):
  id = models.BigAutoField(primary_key=True)
  userName = models.CharField(max_length = 100)
  email = models.EmailField(max_length = 100, unique=True)
  password = models.TextField()
#   idConf = models.OneToOneField()
#   idRol = models.OneToOneField()
  active = models.BooleanField(default=True)