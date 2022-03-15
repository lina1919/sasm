from django.shortcuts import render
from stories import models as story_models
from .serializers import StorySerializer,CommentSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
# Create your views here.
class StoryViewSet(viewsets.ModelViewSet):
    queryset = story_models.Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [AllowAny] #인증적용
    
    def perform_create(self,serializer):
        # post = form.save(commit=False)
        # post.author = self.request.user
        # post.save()
        serializer.save(writer=self.request.user)
        return super().perform_create(serializer)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    @action(detail=True, methods=["POST"])
    def like(self, request, pk):
        post = self.get_object()
        post.like_user_set.add(self.request.user)
        return Response(status.HTTP_201_CREATED)

    @like.mapping.delete
    def unlike(self, request, pk):
        post = self.get_object()
        post.like_user_set.remove(self.request.user)
        return Response(status.HTTP_204_NO_CONTENT)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = story_models.Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(post__pk=self.kwargs["post_pk"])
        return qs

    def perform_create(self, serializer):
        post = get_object_or_404(story_models.Story, pk=self.kwargs["post_pk"])
        serializer.save(writer=self.request.user,post=post)
        return super().perform_create(serializer)