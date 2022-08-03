from typing import ParamSpec
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from datetime import datetime  
from django.core.exceptions import ValidationError

# Create your models here.

class CustomUser(AbstractUser):
    user_type_choices = [('S', 'Seller'), ('C', 'Customer')]
    user_type = models.CharField(max_length = 1, choices = user_type_choices, default = 'C')

class Lot(models.Model):
    # primary key automatically added (integer)    
    flower_type = models.CharField(max_length=30)
    class FlowerColor(models.TextChoices):
        red = 'R', _('Red')
        blue = 'B', _('Blue')
        green = 'G', _('Green')
        #etc
    flower_color = models.CharField(max_length = 1, choices = FlowerColor.choices)
    flower_num = models.IntegerField()
    flower_price_of_single = models.DecimalField(
        max_digits = 10, 
        decimal_places = 2
        )
    is_visible = models.BooleanField(default=True)
    flower_seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        limit_choices_to={'user_type': 'S'}
    )
    def __str__(self) -> str:
        return str(self.flower_type) +' ' + str(self.flower_seller)


class LotsReview(models.Model):
    reviewed_lot = models.ForeignKey('Lot', on_delete = models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        limit_choices_to={'user_type': 'C'}
    )
    review = models.CharField(max_length=500)

class SellerReview(models.Model):
    reviewed_seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        limit_choices_to={'user_type': 'S'}, 
    )

    review = models.CharField(max_length=500)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        limit_choices_to={'user_type': 'C'}, 
        related_name = 'customer'
    )
class Deal(models.Model):
    
    time = models.DateTimeField(default=datetime.now)
    lot = models.ForeignKey(
        'lot', 
        on_delete=models.RESTRICT, 
        )
    amount = models.IntegerField(default=1)

    customer  = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        limit_choices_to={'user_type': 'C'}, 
    ) 
    total_check = models.DecimalField(
        max_digits = 10, 
        decimal_places = 2
    )

    def __str__(self) -> str:
        return str(self.customer) +' '+ str(self.lot)

    def save(self, *args, **kwargs):
        self.total_check = self.amount * self.lot.flower_price_of_single
        related_lot = Lot.objects.get(pk = self.lot.pk)

        if related_lot.flower_num - self.amount < 0:
            #print("Error: Seller don't have enough flowers")
            return ValidationError("Seller don't have enough flowers")

        related_lot.flower_num -= self.amount 
        related_lot.save()
        super(Deal, self).save(*args, **kwargs)

