from django.urls import path     

from . import views


urlpatterns = [
    
    path('', views.index),
    path('login/',views.login),
    path('process_money/<juego>/',views.process_money),	
    path('reset/',views.reset),
]