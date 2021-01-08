from django.conf.urls import url,include
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token
from . import views


# Registration,Login,Forgot,Profile change

urlpatterns=[

    path('jwt/', obtain_jwt_token),
    path('jwt/refresh/', refresh_jwt_token),
    
]