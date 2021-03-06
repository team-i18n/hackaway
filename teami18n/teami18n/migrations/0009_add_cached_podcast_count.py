# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Remember to use orm['appname.ModelName'] rather than "from appname.models..."
        for country in orm["teami18n.Country"].objects.all():
            country.podcasts_count = country.podcasts.count()
            country.save()

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'teami18n.country': {
            'Meta': {'object_name': 'Country'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'podcasts_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'population': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'teami18n.podcast': {
            'Meta': {'object_name': 'Podcast'},
            'countries': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'podcasts'", 'symmetrical': 'False', 'to': u"orm['teami18n.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'program_name': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'show_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'story_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'teaser': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['teami18n']
    symmetrical = True
