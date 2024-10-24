from django.core.management.base import BaseCommand
from apps.approvals.utils.feishu_approvals import sync_feishu_approvals
from apps.approvals.utils.feishu_documents import sync_feishu_documents
from apps.approvals.utils.feishu_sheets import sync_feishu_sheets
from apps.approvals.utils.feishu_multidimensional_sheets import sync_feishu_multidimensional_sheets


class Command(BaseCommand):
    help = '同步 Feishu 数据'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('开始同步 Feishu 数据...'))

        self.stdout.write(self.style.SUCCESS('同步 Feishu 审批流程数据...'))
        sync_feishu_approvals()

        self.stdout.write(self.style.SUCCESS('同步 Feishu 文档数据...'))
        sync_feishu_documents()

        self.stdout.write(self.style.SUCCESS('同步 Feishu 表格数据...'))
        sync_feishu_sheets()

        self.stdout.write(self.style.SUCCESS('同步 Feishu 多维表格数据...'))
        sync_feishu_multidimensional_sheets()

        self.stdout.write(self.style.SUCCESS('同步完成'))
