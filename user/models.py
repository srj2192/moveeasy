from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, timedelta


def default_start_time():
    return datetime.now()+timedelta(hours=8)


def default_end_time():
    return datetime.now()+timedelta(hours=17)


class Address(models.Model):

    class Meta:
        db_table = "user_address"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=500)
    is_default = models.BooleanField(default=True)
    available_from = models.DateTimeField(default=default_start_time)
    available_to = models.DateTimeField(default=default_end_time)

    def __str__(self):
        return "Address saved successfully for User {0}".format(self.user.username)

    def as_dict(self):

        return {
            "user": self.user.username,
            "address": self.address,
            "available_from": self.available_to.strftime("%y/%m/%d %H:%M:%S"),
            "available_to": self.available_from.strftime("%Y/%m/%d %H:%M:%S"),
            "is_default": self.is_default
        }

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Address, self).save()
        return {
            "user": self.user,
            "address": self.address,
            "is_default": self.is_default
        }
