"""Company info urls"""
from django.urls import path
from . import views

urlpatterns = [
    path('faq/', views.faq_page, name='faq'),
    path('shipping_returns/', views.shipping_returns, name='shipping_returns'),
    path('about_us/', views.about_us, name='about_us'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('contact_us/', views.contact, name='contact'),
]
