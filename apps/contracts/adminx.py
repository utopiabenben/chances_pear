import xadmin
from .models import Contract


class ContractAdmin(object):
    list_display = ['contract_number', 'customer', 'signed_date', 'status']
    search_fields = ['contract_number', 'customer__name']
    list_filter = ['status', 'signed_date']


    model_icon = 'fa fa-user'
    app_label = '管理类'  # 自定义分组名称，显示在菜单栏


    def queryset(self):
        qs = super().queryset()
        # Add additional queries if needed
        return qs


try:
    xadmin.site.register(Contract, ContractAdmin)
except xadmin.sites.AlreadyRegistered:
    pass
