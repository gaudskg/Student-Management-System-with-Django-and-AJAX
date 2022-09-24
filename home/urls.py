from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home, name = 'home'),
    path('send_data/', views.send_data, name='send_data')

]
