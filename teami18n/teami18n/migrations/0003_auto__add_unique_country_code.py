# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Country', fields ['code']
        db.create_unique(u'teami18n_country', ['code'])


    def backwards(self, orm):
        # Removing unique constraint on 'Country', fields ['code']
        db.delete_unique(u'teami18n_country', ['code'])


    models = {
        u'teami18n.country': {
            'Meta': {'object_name': 'Country'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['teami18n']