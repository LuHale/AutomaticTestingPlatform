# Generated by Django 2.2.3 on 2019-08-10 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20190722_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='testcase_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testcases.Testcases'),
        ),
    ]