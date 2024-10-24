from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, Count
from apps.contracts.models import Contract
from apps.presales.models import PresalesProject
from apps.projects.models import Project
from apps.customers.models import Customer


class CustomerStatisticsView(APIView):
    def get(self, request):
        # 初始化数据结构，用于合并所有客户数据
        customers = Customer.objects.all().values(
            'id', 'name', 'contract_count', 'total_contract_amount',
            'presales_project_amount', 'completed_receivable_amount',
            'current_project_hours', 'current_project_count',
            'cooperation_start_date', 'status'
        )
        customer_data = {customer['name']: customer for customer in customers}

        try:
            # 合同数据：根据客户名称统计合同数量和合同总额
            contract_data = Contract.objects.values('customer__name').annotate(
                contract_count=Count('id'),
                total_contract_amount=Sum('contract_amount')
            )
            for contract in contract_data:
                customer_name = contract['customer__name']
                if customer_name in customer_data:
                    customer_data[customer_name]['contract_count'] = contract['contract_count']
                    customer_data[customer_name]['total_contract_amount'] = contract['total_contract_amount']
            print("合同数据已合并")
        except Exception as e:
            print(f"合同数据查询错误: {e}")

        try:
            # 售前项目数据：根据客户名称统计售前项目金额
            presales_data = PresalesProject.objects.values('customer__name').annotate(
                presales_project_amount=Sum('project_amount')
            )
            for presales in presales_data:
                customer_name = presales['customer__name']
                if customer_name in customer_data:
                    customer_data[customer_name]['presales_project_amount'] = presales['presales_project_amount']
            print("售前项目数据已合并")
        except Exception as e:
            print(f"售前项目数据查询错误: {e}")

        try:
            # 项目管理数据：根据客户名称统计总投入工时和当前项目数量
            project_data = Project.objects.values('customer__name').annotate(
                invested_hours=Sum('total_hours'),
                current_project_count=Count('id')
            )
            for project in project_data:
                customer_name = project['customer__name']
                if customer_name in customer_data:
                    customer_data[customer_name]['current_project_count'] = project['current_project_count']
                    customer_data[customer_name]['invested_hours'] = project['invested_hours']
            print("项目管理数据已合并")
        except Exception as e:
            print(f"项目管理数据查询错误: {e}")

        # 将客户数据转换为列表格式并返回
        return Response(list(customer_data.values()))
