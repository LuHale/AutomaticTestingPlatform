from django.db import models
from django.core import validators
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extension')
    department = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11, null=False, validators=[validators.RegexValidator("^1([38][0-9]|4[579]|5[0-3,5-9]|6[6]|7[0135678]|9[89])\d{8}$")])

    @receiver(post_save, sender=User)    # 接收来自User模型的save信号
    def create_user_extension(sender, instance, created, **kwargs):
        if created:
            UserExtension.objects.create(user=instance)
        else:
            instance.extension.save()

    class Meta:
        db_table = "userextension"