# Generated by Django 2.2.3 on 2019-08-20 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20190820_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='testcase_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testcases.Testcases'),
        ),
    ]