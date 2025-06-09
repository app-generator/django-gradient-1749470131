# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Product(models.Model):

    #__Product_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Customer(models.Model):

    #__Customer_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)

    #__Customer_FIELDS__END

    class Meta:
        verbose_name        = _("Customer")
        verbose_name_plural = _("Customer")


class Customer_Histor(models.Model):

    #__Customer_Histor_FIELDS__
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(customer, on_delete=models.CASCADE)

    #__Customer_Histor_FIELDS__END

    class Meta:
        verbose_name        = _("Customer_Histor")
        verbose_name_plural = _("Customer_Histor")



#__MODELS__END
