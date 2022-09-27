from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home, name = 'home'),
    path('send_data/', views.send_data, name='send_data'),
    path('delete_data/', views.delete_data, name='delete_data')

]
