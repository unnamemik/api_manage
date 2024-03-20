from django.contrib import admin
from django.urls import path, include

from api_manage import views
from sensors.views import sensor, feedback

urlpatterns = [
    path('', views.index, name='index'),
    path('manager/', include('manager.urls'), name='manager'),
    path('sensor/', sensor, name='sensor'),
    path('feedback/', feedback, name='feedback'),
    path('admin/', admin.site.urls),
]
