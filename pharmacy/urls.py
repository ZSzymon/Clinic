from django.urls import path
from . import views as pharmacy_views

urlpatterns = [
    path('', pharmacy_views.pharmacy_home, name='pharmacy_path'),
    path('prescriptions/', pharmacy_views.prescriptions_doctor, name='prescriptions_path'),
    path('drugs/', pharmacy_views.drugs_doctor, name='drugs_path'),
    path('drugs/update_drug/<str:pk>/',
         pharmacy_views.update_drug, name='update_drug'),
    path('drugs/delete_drug/<str:pk>/',
         pharmacy_views.delete_drug, name='delete_drug'),

    path('prescriptions/update_prescription/<str:pk>/',
         pharmacy_views.update_prescription, name='update_prescription'),

    path('prescriptions/delete_prescription/<str:pk>/',
        pharmacy_views.delete_prescription, name='delete_prescription'),
    path('store', pharmacy_views.store_view,name='store'),

    path('cart', pharmacy_views.cart_detail, name='cart'),

    path('store/add/<str:id>/', pharmacy_views.cart_add, name='cart_add'),
    path('store/item_clear/<int:id>/', pharmacy_views.item_clear, name='item_clear'),
    path('store/item_increment/<int:id>/',
         pharmacy_views.item_increment, name='item_increment'),
    path('store/item_decrement/<int:id>/',
         pharmacy_views.item_decrement, name='item_decrement'),

    path('store/cart_clear/', pharmacy_views.cart_clear, name='cart_clear'),



]
