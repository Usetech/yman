# coding=utf-8
from django.db import models
from mptt.models import MPTTModel
from common.models import UpdatableModel
from products.models import YandexModel, Model


class Region(MPTTModel, YandexModel):
    parent = models.ForeignKey('self', null=True, blank=True)


class Shop(YandexModel):
    """
    Internet-shop who offers a good
    """
    rating = models.FloatField(u"Рейтинг", null=True, blank=True)
    pass


class GrabSession(UpdatableModel):
    """
    Prince grab session
    """
    grab_date_start = models.DateTimeField(u"Дата старта обновления ценовой информации")
    grab_date_end = models.DateTimeField(u"Дата завершения обновления ценовой информации")
    summary = models.TextField(u"Результаты")


class Offer(YandexModel):
    """
    Offer information for good-shop-region
    """
    grab_session = models.ForeignKey(GrabSession, related_name='offers')
    model = models.ForeignKey(Model, related_name='offers', verbose_name=u"Товар")
    region = models.ForeignKey(Region, related_name='offers')
    shop = models.ForeignKey(Shop, related_name='offers')
    onstock = models.BooleanField(u"Наличие", default=True)
    warranty = models.BooleanField(u"Офиц. гарантия", default=True)
    url = models.CharField(u"URL", max_length=2048)
    price = models.DecimalField(u"Цена", null=True, blank=True, decimal_places=3, max_digits=15)
    currency_code = models.CharField(u"Валюта", null=True, blank=True, max_length=20)
    geo_lat = models.FloatField(u"Локация, широта", blank=True, null=True)
    geo_lng = models.FloatField(u"Локация, долгота", blank=True, null=True)
