# Generated by Django 5.2.1 on 2025-05-19 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_shape_wasteinput_shape_adminlog_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wasteinput',
            name='size',
            field=models.IntegerField(),
        ),
    ]
