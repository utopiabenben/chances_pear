# Generated by Django 4.2.5 on 2024-09-14 12:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customers", "0002_alter_customer_options_alter_customer_address_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="address",
            field=models.CharField(max_length=255, verbose_name="地址"),
        ),
        migrations.AlterField(
            model_name="customer",
            name="company_size",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="公司规模"
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="contact_email",
            field=models.EmailField(max_length=254, verbose_name="联系邮箱"),
        ),
        migrations.AlterField(
            model_name="customer",
            name="contact_person",
            field=models.CharField(max_length=255, verbose_name="联系人"),
        ),
        migrations.AlterField(
            model_name="customer",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
        ),
        migrations.AlterField(
            model_name="customer",
            name="industry",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="行业"
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="name",
            field=models.CharField(max_length=255, verbose_name="客户名称"),
        ),
        migrations.AlterField(
            model_name="customer",
            name="phone",
            field=models.CharField(max_length=20, verbose_name="联系电话"),
        ),
        migrations.AlterField(
            model_name="customer",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="更新时间"),
        ),
    ]
