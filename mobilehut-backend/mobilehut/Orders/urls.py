from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    
    url(r'^create_order/$', views.CreateOrder.as_view(), name='CreateOrder'),
    url(r'^manage_order/(?P<id>\d+)/$', views.ManageOrder.as_view(), name='ManageOrder'),
    url(r'^get_order/$', views.GetOrder.as_view(), name='GetOrder'),
    url(r'^create_porder/$', views.CreateProductOrder.as_view(), name='CreateOrder'),
    url(r'^manage_porder/(?P<id>\d+)/$', views.ManageProductOrder.as_view(), name='ManageOrder'),
    url(r'^get_porder/(?P<id>\d+)/$', views.GetPOrder.as_view(), name='GetPOrder'),
    url(r'^create_coupan/$', views.CreateCoupan.as_view(), name='CreateCoupan'),
    url(r'^manage_coupan/(?P<id>\d+)/$', views.ManageCoupan.as_view(), name='ManageCoupan'),
    path('get_discount/<str:coupan>/', views.GetCoupan.as_view(), name='GetCoupan'),
   
]