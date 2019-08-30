from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views
from to_do.views import home

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('api/', include('to_do.urls')),
    path('auth/', include('auth.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('social_auth/', include('social_django.urls', namespace='social')),  # <- Here
    path('', home, name='home'),
]
