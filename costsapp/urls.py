from django.urls import path
from .views import (BoysList, BoysCreate, BoysDelete, BoysUpdate, boys_salary, boys_detail,
GirlsList, GirlsCreate, GirlsDelete, GirlsUpdate, girls_salary, girls_detail,
ShoppingList, ShoppingCreate, ShoppingDelete, ShoppingUpdate, shopping_costs, shopping_detail, profit, signupfunc, loginfunc, logoutfunc)
urlpatterns = [
    path('boyslist/', BoysList, name='boys_list'),
    path('boyscreate/', BoysCreate.as_view(), name='boys_create'),
    path('boysdelete/<int:pk>', BoysDelete.as_view(), name='boys_delete'),
    path('boysupdate/<int:pk>', BoysUpdate.as_view(), name='boys_update'),
    path('boysalary/<int:pk>', boys_salary, name='boys_salary'),
    path('boysdetail/<int:pk>', boys_detail, name='boys_detail'),
    path('girlslist/', GirlsList, name='girls_list'),
    path('girlscreate/', GirlsCreate.as_view(), name='girls_create'),
    path('girlsdelete/<int:pk>', GirlsDelete.as_view(), name='girls_delete'),
    path('girlsupdate/<int:pk>', GirlsUpdate.as_view(), name='girls_update'),
    path('girlsalary/<int:pk>', girls_salary, name='girls_salary'),
    path('girlsdetail/<int:pk>', girls_detail, name='girls_detail'),
    path('shoppinglist/', ShoppingList, name='shopping_list'),
    path('shoppingcreate/', ShoppingCreate.as_view(), name='shopping_create'),
    path('shoppingdelete/<int:pk>', ShoppingDelete.as_view(), name='shopping_delete'),
    path('shoppingupdate<int:pk>/', ShoppingUpdate.as_view(), name='shopping_update'),
    path('shoppingcost/<int:pk>', shopping_costs, name='shopping_costs'),
    path('shoppingdetail/<int:pk>', shopping_detail, name='shopping_detail'),
    path('profit/', profit, name='profit'),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),

]