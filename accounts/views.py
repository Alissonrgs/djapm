# django
from django.contrib.auth.models import User

# third party
from rest_framework.viewsets import ModelViewSet

# local
# from .filters import UserFilter
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    model = User
    # filter_class = UserFilter
    serializer_class = UserSerializer
    search_fields = []
    ordering_fields = []
