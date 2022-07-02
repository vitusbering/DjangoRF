"""DjangoRF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from men.views import *
# from rest_framework import routers


# router = routers.SimpleRouter()
# router = routers.DefaultRouter()
# router.register(r'men', MenViewSet, basename='men')
# print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    # path('api/v1/menlist/', MenAPIView.as_view()),# bind the MenAPIView with path from view.py
    # path('api/v1/menlist/<int:pk>', MenAPIView.as_view()),
    ## path('api/v1/mendetail/<int:pk>', MenAPIDetailView.as_view()),
    # path('api/v1/menlist/', MenViewSet.as_view({'get': 'list'})),
    # path('api/v1/menlist/<int:pk>', MenViewSet.as_view({'put': 'update'})),
    # path('api/v1/', include(router.urls)) # http://127.0.0.1:8000/api/v1/men/
    path('api/v1/men/', MenAPIList.as_view()), # bind the MenAPIView with path from view.py
    path('api/v1/men/<int:pk>/', MenAPIUpdate.as_view()),
    path('api/v1/mendelete/<int:pk>/', MenAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')), #new
    re_path(r'^auth/', include('djoser.urls.authtoken')), #new
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
