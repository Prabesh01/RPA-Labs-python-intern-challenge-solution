from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/list/',views.list, name="list"),
    path('list/',views.show, name="show"),
    path('upload/',views.upload, name="upload"),
    path('api/fee/',views.fee, name="fee"),
]
