from django.db import models


class Testcases(models.Model):
    name = models.CharField(max_length=100)
    describe = models.CharField(max_length=300)
    creat_time = models.DateTimeField(auto_now_add=True, null=True)
    product_id = models.ForeignKey('product.Products', on_delete=models.CASCADE, null=True)
    object_id = models.ForeignKey('object.Objcets', on_delete=models.CASCADE, null=True)
    state = models.BooleanField(default=1)

    class Meta:
        db_table = 'testcases'
