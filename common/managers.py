from django.db import models


class ModeratedObjectManager(models.Manager):
    pass


class UpdatableModelManager(models.Manager):
    def active(self):
        return self.filter(deleted_at__isnull=True)