# from django.db import models
# from django.utils import timezone
# from django.conf import settings
# from accounts.abstract.models import AbstractModel


# class DiaryEntry(AbstractModel):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="diary_entries"
#     )
#     date = models.DateField(auto_now_add=True, null=True)
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     date_created = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name_plural = "Entries"


import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from accounts.abstract.models import AbstractModel, AbstractManager
from django.conf import settings


class DiaryManager(AbstractManager):
    pass


class Diary(AbstractModel):
    date = models.DateField(auto_now_add=True, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    highlight = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    objects = DiaryManager()

    def __str__(self):
        return f"{self.user.name}"
