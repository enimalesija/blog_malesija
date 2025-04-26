from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# Web view: list all posts in the homepage
def post_list(request):
    posts = list(
        Post.objects.all().values('id', 'title', 'content', 'created_at', 'updated_at')
    )
    return render(request, 'posts/post_list.html', {'posts': posts})

# Web view: shows a single post into detailed view
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})

# API: GET list & POST create
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# API: GET single, PUT update, DELETE destroy
class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
