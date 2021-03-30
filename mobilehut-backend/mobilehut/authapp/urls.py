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
    path('manage_user/<id>/', views.ManageUser.as_view(), name='ManageUser'),
    path('account_detail/', views.AccountDetail.as_view(), name='AccountDetail'),
    path('change_password/', views.UpdatePassword.as_view(), name='UpdatePassword'),
    path('create_user_social/',views.CreateSocial.as_view(), name='SocialUser'),
    path('create_contact/', views.CreateContact.as_view(), name='CreateContact'),
    path('view_contact/<pk>/', views.ViewContact.as_view(), name='ViewContact'),

    
]