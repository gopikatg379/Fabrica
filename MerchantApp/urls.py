from django.urls import path
from MerchantApp import views
urlpatterns =[
    path('home',views.merchant_home,name='merchant_home'),
    path('add',views.add_products,name='add_products'),
    path('delete/<int:id>',views.delete_product,name='delete_product')
]