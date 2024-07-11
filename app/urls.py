

from django.urls import path, include

from .views import process_order, checkout,  add_to_cart, show_cart, payment_done, remove_cart, orders, VirtualMachineComparisonView_database, ProductView, ProductDetailView, search_results, CustomerRegistrationView, ProfileView, address, SaveOrderView
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('passwordchange/', auth_views.PasswordChangeView.as_view(), name='passwordchange'),  # Add this line
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('instance_comparison_database/', VirtualMachineComparisonView_database, name='instance_comparison_database'),
    path('process_order/', process_order, name='process_order'),
    path('order_review/', checkout, name='order_review'),
    path('checkout/', checkout, name='checkout'),
    #path('cart/', show_cart, name='cart'),
    #path('add_to_cart/', add_to_cart, name='add_to_cart'),
    # path('plus_cart/', plus_cart, name='plus_cart'),
    # path('minus_cart/', minus_cart, name='minus_cart'),
    #path('remove_cart/', remove_cart, name='remove_cart'),
    #path('payment_done/', payment_done, name='payment_done'),
    path('orders/', orders, name='orders'),
    path('search/', search_results, name='search_results'),
    path('address/', address, name='address'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('registration/', CustomerRegistrationView.as_view(), name='registration'),
    path('', ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
]
