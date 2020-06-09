from django.urls import include, path
from CreditApp import views
from django.contrib import admin, auth

admin.site.site_header = "Panel de Administracion"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('CreditApp/', include('CreditApp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]