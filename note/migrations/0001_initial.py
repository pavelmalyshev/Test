# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Autor'
        db.create_table(u'note_autor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fio', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_birth', self.gf('django.db.models.fields.DateTimeField')()),
            ('bio', self.gf('django.db.models.fields.CharField')(max_length=5000)),
        ))
        db.send_create_signal(u'note', ['Autor'])

        # Adding model 'Stat'
        db.create_table(u'note_stat', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_pub', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=5000)),
            ('autor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['note.Autor'])),
        ))
        db.send_create_signal(u'note', ['Stat'])

        # Adding model 'Comment'
        db.create_table(u'note_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('who', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=5000)),
            ('stat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['note.Stat'])),
        ))
        db.send_create_signal(u'note', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Autor'
        db.delete_table(u'note_autor')

        # Deleting model 'Stat'
        db.delete_table(u'note_stat')

        # Deleting model 'Comment'
        db.delete_table(u'note_comment')


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
            'autor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['note.Autor']"}),
            'date_pub': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '5000'})
        }
    }

    complete_apps = ['note']