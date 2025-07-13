from django.urls import path
from . import views

urlpatterns = [
    path('', views.bakerys_list, name='bakerys_list'),
    path('bakerys/<int:pk>/',views.bakerys_detail,
         name='bakerys_detail'),
]
urlpatterns = [

    path('', views.canteen_list, name='canteen_list'),
    path('canteen/<int:pk>/',views.canteen_detail,
         name='canteen_detail'),

]

urlpatterns = [
    path('', views.mess_list, name='mess_list'),
    path('mess/<int:pk>/',views.mess_detail,
         name='mess_detail'),
    
]
