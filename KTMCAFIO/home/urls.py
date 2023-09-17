from .views import *
from django.urls import path


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact', contact, name='contact'),
    path('menu', MenuView.as_view(), name='menu'),
    path('about', AboutView.as_view(), name='about'),
    path('cart', CartView.as_view(), name = "cart"),
    path('add_to_cart/<slug>', add_to_cart, name='add_to_cart'),
    path('reduce_quantity/<slug>', reduce_quantity, name='reduce_quantity'),
    path('delete_cart/<slug>', delete_cart, name='delete_cart'),
    path('signup', signup, name='signup'),
    path('checkout', CheckoutView.as_view(), name='checkout'),
    path('place-order', CheckoutView.placeorder, name ="placeorder"),
    path('change-order-status/<int:order_id>/<str:new_status>/', change_order_status, name='change-order-status'),
    # path('search', search_menu, name='search_menu')

]