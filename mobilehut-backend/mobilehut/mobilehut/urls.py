from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),
    url(r'^AuthApp/', include('authapp.urls')),
    url(r'^Products/',include('Products.urls')),
    url(r'^Orders/',include('Orders.urls')),
    url(r'^HomePage/',include('Homepage.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
