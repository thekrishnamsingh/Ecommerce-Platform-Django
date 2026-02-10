from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('product/',views.productPage,name='product'),
    path('register/', views.register, name='register'),
    path('login/', views.signin, name='login'),
    path('user/',views.user, name='user'),
    path('orders/',views.orders, name='orders'),
    path('logout/', views.signout, name='logout'),
    path('buynow/', views.buynow, name='buynow'),
    path('checkout/', views.checkout, name='checkout'),
    path('changepass/', views.changepass, name='changepass'),
    path('mycart/', views.mycart, name='mycart'),
    path('update_cart/',views.update_cart, name='update_cart'),
    path('mobile/', views.mobile, name='mobile'),
    path('earbuds/',views.earbuds, name='earbuds'),
    path('laptop/',views.laptop, name='laptop'),
    path('fridge/',views.fridge, name='fridge'),
    path('watch/',views.watch, name='watch'),
    path('fan/',views.fan, name='fan'),
    path('washing/',views.washing, name='washing'),
    path('speakers/',views.speakers, name='speakers'),
]