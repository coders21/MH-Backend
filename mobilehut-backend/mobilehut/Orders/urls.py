from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^create_order/$', views.CreateOrder.as_view(), name='CreateOrder'),
    url(r'^manage_order/(?P<id>\d+)/$', views.ManageOrder.as_view(), name='ManageOrder'),
    url(r'^create_porder/$', views.CreateProductOrder.as_view(), name='CreateOrder'),
    url(r'^manage_porder/(?P<id>\d+)/$', views.ManageProductOrder.as_view(), name='ManageOrder')

]