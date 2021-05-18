"""
tvsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

# from rest_framework.schemas import get_schema_view
# from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
# # 利用get_schema_view()方法，传入两个Render类得到一个schema view
# schema_view = get_schema_view(title='API',renderer_classes=[SwaggerUIRenderer,OpenAPIRenderer])

urlpatterns = [
    # Uncomment the next line to enable the admin:
    #path('admin/', admin.site.urls),
    re_path('^$', TemplateView.as_view(template_name = 'index.html'), name = "index"),
    path('', include('app_basic.urls')),
    path('manage/', include('app_manage.urls')),
    path('api/', include('api.urls')),
    # path('docs/', schema_view, name = "Swagger接口文档")
]