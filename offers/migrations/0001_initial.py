# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Region'
        db.create_table(u'offers_region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.utcnow)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.utcnow, db_index=True)),
            ('revision', self.gf('django.db.models.fields.BigIntegerField')(default=0, db_index=True)),
            ('deleted_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('ya_id', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['offers.Region'], null=True, blank=True)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'offers', ['Region'])

        # Adding model 'Shop'
        db.create_table(u'offers_shop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.utcnow)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.utcnow, db_index=True)),
            ('revision', self.gf('django.db.models.fields.BigIntegerField')(default=0, db_index=True)),
            ('deleted_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('ya_id', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'offers', ['Shop'])

        # Adding model 'GrabSession'
        db.create_table(u'offers_grabsession', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.utcnow)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.utcnow, db_index=True)),
            ('revision', self.gf('django.db.models.fields.BigIntegerField')(default=0, db_index=True)),
            ('deleted_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('grab_date_start', self.gf('django.db.models.fields.DateTimeField')()),
            ('grab_date_end', self.gf('django.db.models.fields.DateTimeField')()),
            ('summary', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'offers', ['GrabSession'])

        # Adding model 'Offer'
        db.create_table(u'offers_offer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.utcnow)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.utcnow, db_index=True)),
            ('revision', self.gf('django.db.models.fields.BigIntegerField')(default=0, db_index=True)),
            ('deleted_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('ya_id', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('grab_session', self.gf('django.db.models.fields.related.ForeignKey')(related_name='offers', to=orm['offers.GrabSession'])),
            ('model', self.gf('django.db.models.fields.related.ForeignKey')(related_name='offers', to=orm['products.Model'])),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(related_name='offers', to=orm['offers.Region'])),
            ('shop', self.gf('django.db.models.fields.related.ForeignKey')(related_name='offers', to=orm['offers.Shop'])),
            ('onstock', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('warranty', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=3, blank=True)),
            ('currency_code', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('geo_lat', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('geo_lng', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'offers', ['Offer'])


    def backwards(self, orm):
        # Deleting model 'Region'
        db.delete_table(u'offers_region')

        # Deleting model 'Shop'
        db.delete_table(u'offers_shop')

        # Deleting model 'GrabSession'
        db.delete_table(u'offers_grabsession')

        # Deleting model 'Offer'
        db.delete_table(u'offers_offer')


    models = {
        u'offers.grabsession': {
            'Meta': {'object_name': 'GrabSession'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            'deleted_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'grab_date_end': ('django.db.models.fields.DateTimeField', [], {}),
            'grab_date_start': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'revision': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow', 'db_index': 'True'})
        },
        u'offers.offer': {
            'Meta': {'object_name': 'Offer'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            'currency_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'deleted_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'geo_lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'geo_lng': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'grab_session': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'offers'", 'to': u"orm['offers.GrabSession']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'offers'", 'to': u"orm['products.Model']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'onstock': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '3', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'offers'", 'to': u"orm['offers.Region']"}),
            'revision': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'offers'", 'to': u"orm['offers.Shop']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow', 'db_index': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'warranty': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ya_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        u'offers.region': {
            'Meta': {'object_name': 'Region'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            'deleted_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['offers.Region']", 'null': 'True', 'blank': 'True'}),
            'revision': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow', 'db_index': 'True'}),
            'ya_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        u'offers.shop': {
            'Meta': {'object_name': 'Shop'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            'deleted_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'revision': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow', 'db_index': 'True'}),
            'ya_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        u'products.category': {
            'Meta': {'object_name': 'Category'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            'deleted_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Category']", 'null': 'True', 'blank': 'True'}),
            'revision': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow', 'db_index': 'True'}),
            'ya_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        u'products.model': {
            'Meta': {'object_name': 'Model'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'models'", 'to': u"orm['products.Category']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            'deleted_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'revision': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow', 'db_index': 'True'}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'models'", 'to': u"orm['products.Vendor']"}),
            'ya_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        u'products.vendor': {
            'Meta': {'object_name': 'Vendor'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            'deleted_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'revision': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow', 'db_index': 'True'}),
            'ya_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['offers']