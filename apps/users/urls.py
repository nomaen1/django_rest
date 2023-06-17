from rest_framework.routers import DefaultRouter

from apps.users.views import UserAPIVIewSet

router = DefaultRouter()
router.register('users', UserAPIVIewSet, "api_users")

urlpatterns = router.urls