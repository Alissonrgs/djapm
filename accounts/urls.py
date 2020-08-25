# third party
from rest_framework.routers import DefaultRouter

# local
from .views import UserViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
urlpatterns = router.urls
