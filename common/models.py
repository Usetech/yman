# coding:utf-8
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
import time
from common.managers import ModeratedObjectManager, UpdatableModelManager
from django.utils.translation import ugettext_lazy as _


def get_updated_at_and_revision():
    updated_at = datetime.utcnow()
    ticks = time.mktime(updated_at.timetuple())*1e+6 + updated_at.microsecond
    return updated_at, ticks


class UpdatableModel(models.Model):
    created_at      = models.DateTimeField(default=datetime.utcnow, verbose_name=_(u"Создано"))
    updated_at      = models.DateTimeField(default=datetime.utcnow, db_index=True, verbose_name=_(u"Обновлено"))
    revision        = models.BigIntegerField(default=0, db_index=True, verbose_name=_(u"Ревизия"))
    deleted_at      = models.DateTimeField(null=True, blank=True, verbose_name=_(u"Удалено"))

    objects         = UpdatableModelManager()

    def _get_is_active(self):
        return self.deleted_at is None

    is_active = property(_get_is_active)

    @staticmethod
    def get_datetime_from_revision(revision):
        return datetime.fromtimestamp(int(revision)*1e-6)

    def save(self, *args, **kwargs):
        upd_at, rev = get_updated_at_and_revision()
        self.updated_at = upd_at
        self.revision = rev
        super(UpdatableModel, self).save(*args, **kwargs)

    def delete(self, using=None, force=False):
        # do not call super's delete because we don't whant to delete object physically
        if force:
            super(UpdatableModel, self).delete(using)
        else:
            self.deleted_at = datetime.utcnow()
            self.save()

    def refresh_from_db(self):
        from_db = self.__class__.objects.get(id=self.pk)
        fields = self.__class__._meta.get_all_field_names()

        #for each field in Model
        for field in fields:
            setattr(self, field, getattr(from_db, field)) #update this instances info from returned Model

    class Meta:
        abstract    = True
        # do not apply ordering because condition occurs in all queries, even sub-queries, which is slow
        # ordering    = ['-updated_at']


class NamedModel(models.Model):
    name        = models.CharField(max_length=256, verbose_name=_(u"Название"))

    def __unicode__(self):
        return self.name

    class Meta:
        abstract    = True
        ordering    = ["name"]


class ModeratedModel(models.Model):
    """Objects with pending moderation"""
    STATE_PENDING = "P"
    STATE_REJECTED = "R"
    STATE_ALLOWED = "A"
    CHOICES_STATE = (
        (STATE_PENDING, "Pending"),
        (STATE_REJECTED, "Rejected"),
        (STATE_ALLOWED, "Allowed")
    )

    state           = models.CharField(max_length=128, choices=CHOICES_STATE, default=STATE_PENDING, verbose_name=_(u"Состояние"))
    moderated_by    = models.ForeignKey(User, null=True, blank=True, related_name="my_moderated_items", verbose_name=_(u"Модератор"))
    objects         = ModeratedObjectManager()

    class Meta:
        abstract = True