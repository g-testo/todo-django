from django.urls import path, include
from rest_framework import routers
from .views import ListViewSet, ItemViewSet

router = routers.DefaultRouter()
router.register(r'lists', ListViewSet)
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]