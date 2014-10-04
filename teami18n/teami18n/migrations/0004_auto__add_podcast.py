# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Podcast'
        db.create_table(u'teami18n_podcast', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('story_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=16)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('teaser', self.gf('django.db.models.fields.TextField')()),
            ('program_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('show_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('image_link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'teami18n', ['Podcast'])


    def backwards(self, orm):
        # Deleting model 'Podcast'
        db.delete_table(u'teami18n_podcast')


    models = {
        u'teami18n.country': {
            'Meta': {'object_name': 'Country'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'teami18n.podcast': {
            'Meta': {'object_name': 'Podcast'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'program_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'show_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'story_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'teaser': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['teami18n']