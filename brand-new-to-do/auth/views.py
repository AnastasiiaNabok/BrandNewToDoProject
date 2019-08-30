from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView


from auth.permission_classes import OnlyForNonAuthorized
from auth.model_serializers import UserSerializer


class CreateUserView(CreateAPIView):

    model = User
    permission_classes = [OnlyForNonAuthorized]
    serializer_class = UserSerializer
