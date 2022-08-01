from typing import ParamSpec
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class CustomUser(AbstractUser):
    pass

    def __str__(self) -> str:
        return self.username

class Lots(models.Model):
    pass

class LotsReviews(models.Model):
    pass

class SellerReviews(models.Model):
    pass
class Deals(models.Model):
    pass