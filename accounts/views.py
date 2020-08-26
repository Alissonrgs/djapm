# django
from django.contrib.auth.models import User

# third party
from rest_framework.viewsets import ModelViewSet

# local
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
