from django.urls import path
from rest_framework.routers import DefaultRouter
from blog.views import home
from blog.viewsets import PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('', home, name='home'),
] + router.urls