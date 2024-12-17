from django.urls import path
from Userapp import views

urlpatterns = [
    path('home', views.user_home),
    path('logout', views.logout, name='logout'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('cart',views.view_cart,name='view_cart'),
    path('add/wishlist/<int:id>',views.add_wishlist,name='add_wishlist'),
    path('view/more/<int:id>',views.view_more,name='view_more'),
    path('add/cart/<int:id>',views.add_cart,name='add_cart'),
    path('remove/cart/<int:id>',views.delete_cart,name='delete_cart'),
]
