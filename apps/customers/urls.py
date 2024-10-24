# customers/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet

# 创建 REST Framework 的默认路由
router = DefaultRouter()
router.register(r'customers', CustomerViewSet)  # 注册 CustomerViewSet 到 '/customers/' 路径

# 将路由器的 URLs 列表包含进来
urlpatterns = [
    path('', include(router.urls)),  # 包含由 DRF 生成的路由
]
