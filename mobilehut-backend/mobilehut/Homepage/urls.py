from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get_home_data/$', views.GetHomeData.as_view(), name='GetHomeData'),

    url(r'^create_carousel/$', views.CreateCarousel.as_view(), name='Carousel'),
    url(r'^manage_carousel/(?P<pk>\d+)/$', views.ManageCarousel.as_view(), name='ManageCarousel'),

    url(r'^create_three_banner/$', views.CreateThreeBanner.as_view(), name='ThreeBanner'),
    url(r'^manage_three_banner/(?P<pk>\d+)/$', views.ManageThreeBanner.as_view(), name='ManageThreeBanner'),

    url(r'^create_one_banner/$', views.CreateOneBanner.as_view(), name='OneBanner'),
    url(r'^manage_one_banner/(?P<pk>\d+)/$', views.ManageOneBanner.as_view(), name='ManageOneBanner'),

    url(r'^create_sale/$', views.CreateSale.as_view(), name='CreateSale'),
    url(r'^manage_sale/(?P<pk>\d+)/$', views.ManageSale.as_view(), name='ManageSale'),

    url(r'^create_product_sale/$', views.CreateProductSale.as_view(), name='CreateProductSale'),
    url(r'^manage_product_sale/(?P<pk>\d+)/$', views.ManageProductSale.as_view(), name='ManageProductSale'),

    url(r'^create_recommended_product/$', views.CreateRecommendedProduct.as_view(), name='CreateRProduct'),
    url(r'^manage_recommended_product/(?P<pk>\d+)/$', views.ManageRecommendedProduct.as_view(), name='ManageRProduct'),

]