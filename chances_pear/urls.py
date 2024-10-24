"""
URL configuration for chances_pear project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from xadmin.plugins import xversion
import xadmin
from chances_pear.settings import MEDIA_ROOT
from django.views.static import serve
from django.conf import settings
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.urls import re_path as url

router = DefaultRouter()


#配置置goods的url

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT}),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title="项目管理")),
    path('api/customers/', include('apps.customers.urls')),  # 包含 customers 应用的路由，路径前缀为 'api/customers/'
    path('api/', include('apps.api.urls')),  # 引入API路由

]