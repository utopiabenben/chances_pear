import xadmin
from .models import Approval

class ApprovalAdmin(object):
    list_display = ['approval_code', 'approval_name', 'applicant', 'status', 'create_time']
    model_icon = 'fa fa-check-square-o'

xadmin.site.register(Approval, ApprovalAdmin)
