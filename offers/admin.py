from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from offers.models import Region, Shop, Offer, GrabSession

__author__ = 'sergio'


admin.site.register(Region, MPTTModelAdmin)
admin.site.register(Shop)
admin.site.register(GrabSession)
admin.site.register(Offer)