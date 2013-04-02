# coding=utf-8
from django.db import models
from easy_thumbnails.fields import ThumbnailerField
from common.models import UpdatableModel

__author__ = 'sergio'


class YandexModel(UpdatableModel):
    """
    Base class for Yandex-based models
    """
    ya_id = models.CharField(u"Идентификатор в Яндксе", max_length=128, null=True, blank=True)
    name = models.CharField(u"Название", max_length=256, null=True, blank=True)

    def __unicode__(self):
        return "[%s] %s" % (self.ya_id, self.name)

    class Meta:
        abstract = True


class Category(YandexModel):
    """
    Category for goods
    """
    parent = models.ForeignKey('self', null=True, blank=True)


class Vendor(YandexModel):
    """
    Producer of goods
    """
    pass


class Model(YandexModel):
    vendor = models.ForeignKey(Vendor, related_name='models', verbose_name=u"Производитель")
    category = models.ForeignKey(Category, related_name='models', verbose_name=u"Категория")
    code = models.CharField(u"Код товара", blank=True, null=True, max_length=128)
    description = models.TextField(u"Описание", null=True, blank=True)
    photo = ThumbnailerField(null=True, blank=True, upload_to="models/%Y/%m")