from django.urls import path
from . import views


urlpatterns = [
    path('',views.apiOverview),
    path('owner_list/',views.owner_list,name='owner_list'),
    path('owner_detail/<str:pk>/',views.owner_detail, name='owner_detail'),
    path('hh_list/',views.hh_list,name='hh_list'),
    path('hh_detail/<str:pk>',views.hh_detail,name='hh_detail'),
    path('room_list/',views.room_list,name='room_list'),
    path('room_detail/<str:pk>/',views.room_detail,name='room_detail')
]