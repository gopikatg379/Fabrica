from django.urls import path
from . import views
urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('',views.home,name='home'),
    path('clothes/<int:id>',views.tshirt,name='tshirt'),
    path('dress/<int:id>',views.men_dress,name='men'),
]