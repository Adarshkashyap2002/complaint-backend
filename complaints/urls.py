from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComplaintViewSet
from django.urls import path
from .views import create_user

router = DefaultRouter()
router.register(r'complaints', ComplaintViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from .views import create_user

urlpatterns += [
    path("create-user/", create_user),
]