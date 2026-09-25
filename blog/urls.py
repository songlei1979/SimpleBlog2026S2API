from django.urls import path
from rest_framework.routers import DefaultRouter
from blog.views import home, author_detail
from blog.viewsets import PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('author/<int:pk>',
         author_detail,
         name='author_detail'),
] + router.urls