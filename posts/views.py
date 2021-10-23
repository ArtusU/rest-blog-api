from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer, PostCreateSerialiser, PostUpdateeSerializer


class PostListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class PostCreateView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PostCreateSerialiser

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostUpdateview(generics.UpdateAPIView):
    permission_classe = [permissions.AllowAny]
    serializer_class = PostUpdateeSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'

