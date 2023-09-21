from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('funkos/',views.funkos_index,name='index'),
    path('funkos/<int:funko_id>/',views.funkos_detail,name='detail')
]