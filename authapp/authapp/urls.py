
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('seriapp.urls')),
    path('api/token', TokenObtainPairView.as_view(), name='Token_obain_pair'),
    path('api/token/refresh', TokenObtainPairView.as_view(), name='token_refresh'),
   
]
