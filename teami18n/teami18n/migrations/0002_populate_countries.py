# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from django_countries import countries


class Migration(DataMigration):

    def forwards(self, orm):
        for code, __ in countries:
            country, __ = orm.Country.objects.get_or_create(code=code)

    def backwards(self, orm):
        pass

    models = {
        u'teami18n.country': {
            'Meta': {'object_name': 'Country'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['teami18n']
    symmetrical = True
