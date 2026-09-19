from django.db import models


class BlogAnnouncement(models.Model):
    title = models.CharField(max_length=31)
    content = models.TextField()
    title_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    creator = models.ForeignKey('profiler.Profile', on_delete=models.CASCADE)