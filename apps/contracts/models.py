from django.db import models
from apps.customers.models import Customer
from django.utils import timezone

class Contract(models.Model):

    # 合同编号
    contract_number = models.CharField(verbose_name="合同编号", max_length=100, default="未定义")
    # 合同名称
    contract_name = models.CharField(max_length=255, verbose_name="合同名称", default="未命名合同")
    # 客户
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="客户")
    # 合同金额
    contract_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="合同金额", default=0.00)
    # 签署日期
    signed_date = models.DateField(verbose_name="签署日期", default=timezone.now)
    # 创建时间
    created_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    # 更新时间
    updated_at = models.DateTimeField(verbose_name="更新时间", auto_now=True)
    # 状态
    status = models.CharField(verbose_name="状态", max_length=20, default="active")

    class Meta:
        verbose_name = "合同"
        verbose_name_plural = "合同管理"

    def __str__(self):
        return self.contract_name

