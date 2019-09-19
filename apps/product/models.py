from django.db import models


class Products(models.Model):
    object_id = models.ForeignKey('object.Objcets', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    url = models.URLField()
    creat_time = models.DateTimeField(auto_now_add=True, null=True)
    describe = models.TextField(max_length=1000)
    state = models.BooleanField(default=1)

    class Meta:
        db_table = 'products'