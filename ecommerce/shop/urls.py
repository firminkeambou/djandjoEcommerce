from django.urls import path
from . import views

# this set the namespace and all named defined in here are only available for this app, example 'shop:update_item' ("accessing a path")
app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),    # get all item
    path('product/<int:product_id>/', views.detail,
         name='detail'),
]