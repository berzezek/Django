# 1.5 В этом файле можно отслеживать сигналы
from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save # следить когда идут изменения
from django.dispatch import receiver # Декоратор при изменении

@receiver(post_save, sender=User) # при создании
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User) # при обновлении
def create_profile(sender, instance, **kwargs):
    instance.objects.save()

# далее подключаем сигналы в приложении apps.py 1.6
