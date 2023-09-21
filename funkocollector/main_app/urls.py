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
]