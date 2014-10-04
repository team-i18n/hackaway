# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field countries on 'Podcast'
        db.create_table(u'teami18n_podcast_countries', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('podcast', models.ForeignKey(orm[u'teami18n.podcast'], null=False)),
            ('country', models.ForeignKey(orm[u'teami18n.country'], null=False))
        ))
        db.create_unique(u'teami18n_podcast_countries', ['podcast_id', 'country_id'])


    def backwards(self, orm):
        # Removing M2M table for field countries on 'Podcast'
        db.delete_table('teami18n_podcast_countries')


    models = {
        u'teami18n.country': {
            'Meta': {'object_name': 'Country'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'teami18n.podcast': {
            'Meta': {'object_name': 'Podcast'},
            'countries': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'podcasts'", 'symmetrical': 'False', 'to': u"orm['teami18n.Country']"}),
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