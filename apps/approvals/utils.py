import requests
from apps.approvals.models import Approval

FEISHU_APP_ID = 'cli_9f6864e72bb6d00e'
FEISHU_APP_SECRET = '6nboFKFZyRwLXEDJzCclyhno8agvuByb'


# 获取 access token
def get_access_token():
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    payload = {
        "app_id": FEISHU_APP_ID,
        "app_secret": FEISHU_APP_SECRET
    }
    headers = {
        'Content-Type': 'application/json; charset=utf-8'
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        token_data = response.json()
        if token_data['code'] == 0:
            access_token = token_data['tenant_access_token']
            print("获取到新的 tenant_access_token:", access_token)
            return access_token
        else:
            print(f"获取 Access Token 失败，错误码: {token_data['code']}, 错误描述: {token_data['msg']}")
            return None
    else:
        print(f"获取 Access Token 失败，状态码: {response.status_code}, 错误信息: {response.text}")
        return None


# 获取审批实例列表
import datetime


def get_approval_instance_list(access_token, approval_code):
    url = "https://open.feishu.cn/open-apis/approval/v4/instances/query"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json; charset=utf-8"
    }

    # 设置查询条件，比如过去30天的审批实例
    now = datetime.datetime.utcnow()
    start_time = (now - datetime.timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
    end_time = now.strftime("%Y-%m-%dT%H:%M:%SZ")

    payload = {
        "approval_code": "1CA82143-04F2-4580-B5CC-F6089B9A5681",  # 必填的审批流程代码
        "start_time": start_time,  # 添加开始时间，必须是 UTC 格式
        "end_time": end_time,  # 添加结束时间，必须是 UTC 格式
        "page_size": 10  # 设置每页大小
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"获取审批实例失败，状态码: {response.status_code}, 错误信息: {response.text}")
        return None


# 同步 Feishu 审批流程数据
def sync_feishu_approvals():
    print("开始同步 Feishu 审批流程数据...")

    # 获取 access token
    access_token = get_access_token()
    if not access_token:
        print("获取 Access Token 失败，无法继续")
        return

    approval_code = 'your_approval_code_here'  # 需要替换为实际的审批模板代码

    # 获取审批实例列表
    approval_instances = get_approval_instance_list(access_token, approval_code)
    if not approval_instances:
        print("没有审批数据")
        return

    # 打印前5个审批流程数据
    items = approval_instances.get('data', {}).get('items', [])
    for i, instance in enumerate(items[:5]):
        print(f"审批实例 {i + 1}: {instance}")

    # 遍历并保存审批实例
    for instance in items:
        instance_code = instance.get('instance_code')
        approval_name = instance.get('approval_code')

        # 创建或更新审批流程记录
        approval, created = Approval.objects.update_or_create(
            instance_code=instance_code,
            defaults={
                'approval_name': approval_name,
                # 根据实际数据结构保存更多字段
            }
        )

        if created:
            print(f"新增审批流程: {approval_name}")
        else:
            print(f"更新审批流程: {approval_name}")

    print("Feishu 审批流程数据同步完成")
