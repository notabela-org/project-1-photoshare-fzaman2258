from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from blog.models import Post


@receiver(post_save, sender=Post)
def save_post(sender, instance, **kwargs):
    instance.post.save()
    