from django.db import models
from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class GroupExtension(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE, related_name='group_extension')
    create_time = models.DateTimeField(auto_now_add=True)
    create_user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='group_user', null=True)
    group_state = models.BooleanField(default=True)
    update_time = models.DateTimeField(auto_now=True)

    @receiver(post_save, sender=Group)
    def create_group_extension(sender, instance, created, **kwargs):
        if created:
            GroupExtension.objects.create(group=instance)
        else:
            instance.group_extension.save()

    class Meta:
        db_table = 'groupextension'