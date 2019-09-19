from django.db import models


class Objcets(models.Model):
    object_name = models.CharField(max_length=100)
    object_describe = models.TextField(max_length=1000)
    object_createtime = models.DateTimeField(auto_now_add=True, null=True)
    object_state = models.BooleanField(default=1)

    class Meta:
        db_table = 'objects'
        ordering = ['pk']

