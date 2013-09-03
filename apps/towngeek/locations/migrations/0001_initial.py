# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'City'
        db.create_table(u'locations_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=511)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=9)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=9)),
        ))
        db.send_create_signal(u'locations', ['City'])


    def backwards(self, orm):
        # Deleting model 'City'
        db.delete_table(u'locations_city')


    models = {
        u'locations.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '9'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '9'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'})
        }
    }

    complete_apps = ['locations']