import xadmin
from .models import Customer

import xadmin
from .models import Customer


class CustomerAdmin:
    # 显示在列表中的字段
    list_display = ['name', 'cooperation_start_date', 'contract_count',
                    'total_contract_amount', 'presales_project_amount',
                    'completed_receivable_amount', 'current_project_hours',
                    'current_project_count', 'created_at', 'updated_at']

    # 搜索字段
    search_fields = ['name']

    # 列表过滤器
    list_filter = ['cooperation_start_date', 'created_at', 'updated_at']

    # 自定义排序
    ordering = ['-created_at']

    # 自定义字段显示格式
    def total_contract_amount_display(self, obj):
        return f"{obj.total_contract_amount:.2f} 元"

    total_contract_amount_display.short_description = '累计合同总额 (元)'

    def presales_project_amount_display(self, obj):
        return f"{obj.presales_project_amount:.2f} 元"

    presales_project_amount_display.short_description = '售前项目金额 (元)'

    def completed_receivable_amount_display(self, obj):
        return f"{obj.completed_receivable_amount:.2f} 元"

    completed_receivable_amount_display.short_description = '已完成待收款金额 (元)'


# 注册管理类

try:
    xadmin.site.register(Customer, CustomerAdmin)
except xadmin.sites.AlreadyRegistered:
    pass
