from django.contrib import admin
from django.urls import path
from apis.views import VendorList, Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vendors/', VendorList.as_view(), name='vendorlist'),
    path('', Index, name='home'),
]
