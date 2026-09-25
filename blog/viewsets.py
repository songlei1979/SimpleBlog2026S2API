from rest_framework import viewsets, permissions
from blog.models import Post
from blog.permissions import isOwnerOrReadOnly
from blog.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        isOwnerOrReadOnly
    ]

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def get_permissions(self):
        # Apply IsAuthenticated only to the 'create' action
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        elif self.action == 'destroy':
            return [permissions.IsAuthenticated()]
        elif self.action == 'update':
            return [permissions.IsAuthenticated()]
        elif self.action == 'partial_update':
            return [permissions.IsAuthenticated()]
        elif self.action == 'list':
            return [permissions.AllowAny()]
        elif self.action == 'retrieve':
            return [permissions.AllowAny()]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, serializer):
        serializer.save()

    def perform_partial_update(self, serializer):
        serializer.save()