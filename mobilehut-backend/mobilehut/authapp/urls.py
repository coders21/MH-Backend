from django.conf.urls import url,include
from django.urls import path
#from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from . import views


# Registration,Login,Forgot,Profile change

urlpatterns=[

    path('jwt/', views.CustomTokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(),name='token_refresh'),
    path('create_user/', views.CreateUser.as_view(), name='CreateUser'),
    path('manage_user/<int:id>/', views.ManageUser.as_view(), name='ManageUser'),
    path('account_detail/', views.AccountDetail.as_view(), name='AccountDetail'),
    
]