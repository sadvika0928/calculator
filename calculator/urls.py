from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('hello/<str:result.html',views.hello,name = 'hello'),
]