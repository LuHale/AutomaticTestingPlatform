from django.db import models


class Task(models.Model):

    object_id = models.IntegerField(null=False, default=None)
    product_id = models.IntegerField(null=False, default=None)
    testcases = models.CharField(max_length=2048)

    choice = (
        (1, '单次'),
        (2, '多次'),
        (3, '循环'),
    )
    execute_ways = models.IntegerField(choices=choice)
    time = models.CharField(max_length=20, null=False, default=None)
    # thumbnail = models.FileField(upload_to="%Y/%m/%d/", null=False)

    class Meta:
        db_table = 'task'