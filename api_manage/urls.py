from django.contrib import admin
from django.urls import path, include

from api_manage import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('manager/', include('manager.urls'), name='manager'),
    path('admin/', admin.site.urls),
]
