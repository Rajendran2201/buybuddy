from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
  # Primary URLs
    path("", views.index, name="index"),
    path("food-truck", views.foodtruck, name="foodtruck"),
    path("gallery", views.gallery, name="gallery"),
    path("about", views.about, name="about"),
    path("contact-us", views.contactus, name="contactus"),

  # Secondary views: Food Truck
    path('food-truck/location/', views.location, name='location'),
    path('food-truck/orders/', views.orders, name='orders'),
    path('food-truck/events/', views.events, name='events'),
    path('food-truck/events/register', views.registerevent, name='registerevent'),

    # Secondary views: Gallery
    path('gallery/moments/', views.moments, name='moments'),
    path('gallery/blog/', views.blog, name='blog'),

    # Secondary views: About
    path('about/us/', views.aboutus, name='aboutus'),
    path('about/careers/', views.careers, name='careers'),

    path('download-invoice/', views.download_invoice, name='download_invoice'),
    path('cart/update/', views.update_cart_quantity, name='update_cart_quantity'),
    path('cart/remove/', views.remove_from_cart, name='remove_from_cart'),


    # Secondary views: Contact
    path('contact-us/donate/', views.donate, name='donate'),

     # Tertiary views: Contact
    path('food-truck/orders/preorder/', views.preorder, name='preorder'),
    path('food-truck/orders/orderonline/', views.orderonline, name='orderonline'),
    path('food-truck/orders/storefront/', views.storefront, name='storefront'),

     path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

]