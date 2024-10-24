# Generated by Django 4.2.5 on 2024-09-14 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_alter_project_options_project_customer_and_more"),
        ("taskms", "0003_alter_task_name_alter_task_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="project",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="projects.project",
                verbose_name="所属项目",
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.CharField(
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
                verbose_name="任务状态",
            ),
        ),
    ]
