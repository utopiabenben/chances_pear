# Generated by Django 4.2.5 on 2024-09-14 11:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taskms", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="name",
            field=models.CharField(default="默认任务名称", max_length=100, unique=True),
        ),
    ]
