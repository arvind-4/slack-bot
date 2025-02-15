from django.db import models

class Conversation(models.Model):
    channel_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp']
