from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token

from auth.views import CreateUserView


urlpatterns = [
    url(r'login/', obtain_auth_token, name='api'),
    url(r'create/', CreateUserView.as_view(), name='api'),
]
