from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from blog.models import Post
from blog.serializers import PostSerializer


# Create your views here.
@api_view(['GET'])
def home(request):
    posts = PostSerializer(Post.objects.all(), many=True)
    return JsonResponse(posts.data, safe=False)

