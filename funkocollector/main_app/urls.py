from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('funkos/',views.funkos_index,name='index'),
    path('funkos/<int:funko_id>/',views.funkos_detail,name='detail'),
    path('funkos/create/',views.FunkoCreate.as_view(),name='funkos_create'),
    path('funkos/<int:pk>/update/', views.FunkoUpdate.as_view(), name='funkos_update'),
    path('funkos/<int:pk>/delete/', views.FunkoDelete.as_view(), name='funkos_delete'),
    path('funkos/<int:funko_id>/add_buyer/', views.add_buyer, name='add_buyer'),
    path('admirers/create/',views.AdmirerCreate.as_view(),name='admirers_create'),
    path('admirers/', views.AdmirerList.as_view(), name='admirers_index'),
    path('admirers/<int:pk>/', views.AdmirerDetail.as_view(), name='admirers_detail'),
    path('admirers/<int:pk>/update/', views.AdmirerUpdate.as_view(), name='admirers_update'),
    path('admirers/<int:pk>/delete/', views.AdmirerDelete.as_view(), name='admirers_delete'),
    path('cats/<int:funko_id>/assoc_toy/<int:admirer_id>/', views.assoc_admirer, name='assoc_admirer'),
    path('cats/<int:funko_id>/unassoc_toy/<int:admirer_id>/', views.unassoc_admirer, name='unassoc_admirer'),
    
]