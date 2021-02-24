from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^create_category/$', views.CreateCategory.as_view(), name='CreateCategory'),
    url(r'^get_categories/$', views.CreateCategory.as_view(), name='GetCategory'),
    url(r'^manage_categories/(?P<id>\d+)/$', views.ManageCategory.as_view(), name='ManageCategory'),

    url(r'^create_brand/$', views.CreateBrand.as_view(), name='CreateBrand'),
    url(r'^get_brand/$', views.CreateBrand.as_view(), name='GetBrand'),
    url(r'^manage_brand/(?P<id>\d+)/$', views.ManageBrand.as_view(), name='ManageBrand'),

    url(r'^create_model/$', views.CreateModel.as_view(), name='CreateModel'),
    url(r'^get_model/$', views.CreateModel.as_view(), name='GetModel'),
    url(r'^manage_model/(?P<id>\d+)/$', views.ManageModel.as_view(), name='ManageModel'),

    url(r'^create_products/$', views.CreateProduct.as_view(), name='CreateProduct'),
    url(r'^get_products/$', views.CreateProduct.as_view(), name='CreateProduct'),
    url(r'^manage_products/(?P<id>\d+)/$', views.ManageProduct.as_view(), name='ManageProduct'),

    url(r'^create_colour/$', views.CreateColour.as_view(), name='CreateColour'),
    url(r'^get_colour/$', views.CreateColour.as_view(), name='GetColour'),
    url(r'^manage_colour/(?P<id>\d+)/$', views.ManageColour.as_view(), name='ManageColour'),

    url(r'^create_image/$', views.CreateProductImages.as_view(), name='CreateImages'),
    url(r'^manage_images/(?P<id>\d+)/$', views.ManageProductImages.as_view(), name='EditImages'),

    url(r'^get_total/$', views.GetTotal.as_view(), name='Total'),
    url(r'^get_specific_product/(?P<id>\d+)/$', views.DetailProduct.as_view(), name='DetailProduct')

]