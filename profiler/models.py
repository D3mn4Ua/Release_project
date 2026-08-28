from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def profile_saver(sender, instance, created, **kwargs):
    if created == True:
        Profile.objects.create(user=instance)
    else :
        if hasattr(instance, 'profile'):
            instance.profile.save()

class Profile(models.Model):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    ROLE_CHOICES = [
        (USER, 'User'),
        (MODERATOR, 'Moderator'),
        (ADMIN, 'Admin')
    ]

    role = models.CharField(max_length=9, choices=ROLE_CHOICES, default=USER)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    avatar =models .ImageField (upload_to ='avatars/', default ='avatars/default.png')

    def __str__(self):
        return f'Profile of {self.user.username}; role: {self.role}'

    def _sync_role_from_user(self):
        if self.user_id:
            if self.user.is_superuser:
                self.role = self.ADMIN
            elif self.user.is_staff:
                self.role = self.MODERATOR
            else:
                self.role = self.USER

    def save(self, *args, **kwargs):
        self._sync_role_from_user()
        super().save(*args, **kwargs)

    def auto_give_role(self):
        self._sync_role_from_user()
        self.save ()
