# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Stat.about'
        db.add_column(u'note_stat', 'about',
                      self.gf('django.db.models.fields.TextField')(max_length=1000, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Stat.about'
        db.delete_column(u'note_stat', 'about')


    models = {
        u'note.autor': {
            'Meta': {'object_name': 'Autor'},
            'bio': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'date_birth': ('django.db.models.fields.DateTimeField', [], {}),
            'fio': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'note.comment': {
            'Meta': {'object_name': 'Comment'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['note.Stat']"}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '5000'}),
            'who': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'note.stat': {
            'Meta': {'object_name': 'Stat'},
            'about': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True'}),
            'autor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['note.Autor']"}),
            'date_pub': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '5000'})
        }
    }

    complete_apps = ['note']