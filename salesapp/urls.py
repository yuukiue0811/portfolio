from django.urls import path 
from .views import billfunc, taxfunc, SalesCreate,detailfunc, HomeClass, SalesDelete, SalesUpdate, SaleList

urlpatterns = [
    path('', HomeClass.as_view(), name='home'),
    path('list/', SaleList, name='list'),
    path('bill/<int:pk>', billfunc, name='bill'),
    path('tax/<int:pk>', taxfunc, name='tax'),
    path('create/', SalesCreate.as_view(), name='create'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('delete/<int:pk>', SalesDelete.as_view(), name='delete'),
    path('update/<int:pk>', SalesUpdate.as_view(), name='update'),
]