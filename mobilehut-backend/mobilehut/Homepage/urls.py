from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get_home_data/$', views.GetHomeData.as_view(), name='GetHomeData'),
]