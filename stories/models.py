from django.db import models
from core import models as core_models
# Create your models here.

class Photo(core_models.TimeStampedModel):
    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    story = models.ForeignKey("Story", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

class Story(core_models.TimeStampedModel):
    """Room Model Definition"""

    title = models.CharField(max_length=140)
    description = models.TextField()
    address = models.ForeignKey("places.Place", on_delete=models.CASCADE)
    writer = models.ForeignKey("users.User", on_delete=models.CASCADE)
    like = models.ManyToManyField("users.User",related_name='likes',blank=True)
    like_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title

class Comment(core_models.TimeStampedModel):
    """Place Model Definition"""
    content = models.TextField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post = models.ForeignKey('stories.Story', on_delete=models.CASCADE)
    location = models.ForeignKey('places.Place', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.location 
