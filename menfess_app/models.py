from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class Menfess(models.Model):
    from_name = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateTimeField(default=timezone.localtime(timezone.now()))
    slug = models.SlugField(unique=True, blank=True)
      
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = str(uuid.uuid4())[:8]
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.from_name

class Reply(models.Model):
    menfess = models.ForeignKey(Menfess, on_delete=models.CASCADE)
    from_reply_name = models.CharField(max_length=255)
    reply_message = models.TextField()
    reply_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.from_reply_name
    