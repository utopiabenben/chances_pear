# Generated by Django 4.2.5 on 2024-09-14 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("projects", "0002_alter_project_options_project_customer_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(default="默认任务标题", max_length=255)),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="任务描述"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending_schedule", "待排期"),
                            ("scheduled", "已排期"),
                            ("in_development", "研发中"),
                            ("pending_testing", "待测试"),
                            ("in_testing", "测试中"),
                            ("pending_package", "待出包"),
                            ("pending_upgrade", "待升级"),
                            ("completed", "完成"),
                            ("paused", "暂停"),
                            ("cancelled", "取消"),
                        ],
                        default="pending_schedule",
                        max_length=20,
                    ),
                ),
                (
                    "assigned_to",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="负责人"
                    ),
                ),
                (
                    "due_date",
                    models.DateField(blank=True, null=True, verbose_name="截止日期"),
                ),
                ("completed", models.BooleanField(default=False, verbose_name="是否完成")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="更新时间"),
                ),
                (
                    "project",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projects.project",
                    ),
                ),
            ],
            options={
                "verbose_name": "任务",
                "verbose_name_plural": "任务管理",
            },
        ),
    ]
