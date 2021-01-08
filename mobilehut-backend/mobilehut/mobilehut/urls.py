from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

urlpatterns = [
    
    path('admin/', admin.site.urls),
    url(r'^AuthApp/', include('authapp.urls')),
    url(r'^Products/',include('Products.urls'))
   
]
