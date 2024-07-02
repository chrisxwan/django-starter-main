from django.db import models

from backend.models import UUIDBaseModel


class Brand(UUIDBaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
