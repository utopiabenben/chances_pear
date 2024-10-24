from django.db import models

class Approval(models.Model):
    approval_code = models.CharField(max_length=255, verbose_name='审批编号')
    approval_name = models.CharField(max_length=255, verbose_name='审批名称')
    applicant = models.CharField(max_length=255, verbose_name='申请人')
    status = models.CharField(max_length=50, verbose_name='审批状态')
    create_time = models.DateTimeField(verbose_name='创建时间')

    class Meta:
        verbose_name = '审批流程'
        verbose_name_plural = '审批流程管理'
