# Generated by Django 2.2.3 on 2019-08-17 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20190817_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='testcase_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testcases.Testcases'),
        ),
    ]