from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    MASSEGE = 'message'
    FOLLOWER = 'follower'
    LIKE = 'like'
    MENTION = 'mention'

    CHOICES = (
        (MASSEGE, 'Message'),
        (FOLLOWER, 'Follower'),
        (LIKE, 'Like'),
        (MENTION, 'Mention')
    )

    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='notifications')
    notification_type = models.CharField(max_length=20, choices=CHOICES)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='creatednotifications')

    class Meta:
        ordering = ['-created_at']
