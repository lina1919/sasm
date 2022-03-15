from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import StoryViewSet,CommentViewSet

router = DefaultRouter()
router.register('story',StoryViewSet)
router.register(r"story/(?P<post_pk>\d+)/comments", CommentViewSet)
urlpatterns =[
    path('api/',include(router.urls)),
]
