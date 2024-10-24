# Generated by Django 4.2.5 on 2024-10-22 08:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("presales", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="presalesproject",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="创建时间",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="presalesproject",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="更新时间"),
        ),
    ]
