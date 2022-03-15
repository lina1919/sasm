from django.contrib.auth import get_user_model
from rest_framework import serializers
from stories import models as story_models
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id","username","email","gender","nickname","birthdate"]

class StorySerializer(serializers.ModelSerializer):
    writer = AuthorSerializer(read_only=True)
    is_like = serializers.SerializerMethodField("is_like_field")

    def is_like_field(self, story):
        if "request" in self.context:
            user = self.context["request"].user
            return story.like_user_set.filter(pk=user.pk).exists()
        return False

    class Meta:
        model = story_models.Story
        fields = [
            'id',
            'writer',
            'address',
            'created',
            'updated',
            'is_like',
            'like_user_set',
            ]

class CommentSerializer(serializers.ModelSerializer):
    writer = AuthorSerializer(read_only=True)
    class Meta:
        model = story_models.Comment
        fields = ["id", "writer", "content", "created"]