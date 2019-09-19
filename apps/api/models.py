from django.db import models


class Api(models.Model):
    name = models.CharField(max_length=100)
    api_url = models.CharField(max_length=200)
    testcase_id = models.ForeignKey('testcases.Testcases', on_delete=models.CASCADE)
    state = models.BooleanField(default=1)
    method = models.CharField(max_length=20)
    agreement = models.CharField(max_length=20)
    describe = models.TextField(max_length=1000)
    parameter = models.CharField(max_length=2048)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    assert_info = models.CharField(max_length=100, null=True)
    re_func = models.CharField(max_length=200, null=True)
    re_name = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'api'


