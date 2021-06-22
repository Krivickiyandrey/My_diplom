from django.contrib import admin
from django.urls import path
from MotoMarket.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', index, name='index'),
    # path(r'index/', index, name='index'),
    path(r'list/<str:moto_type>/', moto_list, name='moto_list'),
    path(r'detail/<str:moto_type>/<int:pk>/', moto_detail, name='moto_detail'),
    # path(r'SB/', SB, name='SB'),
    # path(r'SB/<int:sportbike_id>/', find_SB, name='find_SB'),
    #
    # path(r'cruisers/', Cruisers, name='cruisers_list'),
    # path(r'cruiser/<int:cruiser_id>/', find_Cruiser, name='find_cruiser'),
    #
    # path(r'enduros/', Enduros, name='enduro_list'),
    # path(r'enduro/<int:enduro_id>/', find_Enduro, name='find_enduro'),
    #
    # path(r'quadros/', quadros, name='quadro_list'),
    # path(r'quadro/<int:quadro_id>/', find_Quadro, name='find_quadro'),

    path(r'cart/<str:moto_type>/<int:pk>/add/', add_to_cart_moto, name='add_to_cart'),
    path(r'cart/<str:moto_type>/<int:pk>/del/', delete_from_cart_moto, name='delete_from_cart'),
    path(r'cart/', shopping_cart, name='cart_detail'),

    path(r'cart/<str:moto_type>/<int:pk>/deal/', deal, name='deal'),

    path(r'sort-by-country/<int:country_id>/', sort_by_country, name='sort_by_country'),
]
