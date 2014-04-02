# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Avaliation'
        db.delete_table('core_avaliation')

        # Adding model 'Avaliacao'
        db.create_table('core_avaliacao', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ponto', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['core.Ponto'])),
            ('acesso', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('acesso_desc', self.gf('django.db.models.fields.TextField')()),
            ('abrigo', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('abrigo_desc', self.gf('django.db.models.fields.TextField')()),
            ('piso', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('piso_desc', self.gf('django.db.models.fields.TextField')()),
            ('rampa', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('rampa_desc', self.gf('django.db.models.fields.TextField')()),
            ('calcada', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('calcada_desc', self.gf('django.db.models.fields.TextField')()),
            ('plataforma', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('plataforma_desc', self.gf('django.db.models.fields.TextField')()),
            ('transito', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('transito_desc', self.gf('django.db.models.fields.TextField')()),
            ('equipamento', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('equipamento_desc', self.gf('django.db.models.fields.TextField')()),
            ('identificacao', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('identificacao_desc', self.gf('django.db.models.fields.TextField')()),
            ('piso_tatil', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('piso_tatil_desc', self.gf('django.db.models.fields.TextField')()),
            ('linhas', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('linhas_desc', self.gf('django.db.models.fields.TextField')()),
            ('logradouro', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('logradouro_desc', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('core', ['Avaliacao'])


    def backwards(self, orm):
        # Adding model 'Avaliation'
        db.create_table('core_avaliation', (
            ('ponto', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['core.Ponto'])),
            ('linhas_desc', self.gf('django.db.models.fields.TextField')()),
            ('transito', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('equipamento', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('calcada', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('rampa_desc', self.gf('django.db.models.fields.TextField')()),
            ('piso_desc', self.gf('django.db.models.fields.TextField')()),
            ('linhas', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('logradouro', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('transito_desc', self.gf('django.db.models.fields.TextField')()),
            ('piso_tatil_desc', self.gf('django.db.models.fields.TextField')()),
            ('identificacao_desc', self.gf('django.db.models.fields.TextField')()),
            ('acesso', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('identificacao', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('rampa', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('plataforma', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('plataforma_desc', self.gf('django.db.models.fields.TextField')()),
            ('piso', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('acesso_desc', self.gf('django.db.models.fields.TextField')()),
            ('abrigo_desc', self.gf('django.db.models.fields.TextField')()),
            ('equipamento_desc', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('abrigo', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('calcada_desc', self.gf('django.db.models.fields.TextField')()),
            ('piso_tatil', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('logradouro_desc', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('core', ['Avaliation'])

        # Deleting model 'Avaliacao'
        db.delete_table('core_avaliacao')


    models = {
        'core.avaliacao': {
            'Meta': {'object_name': 'Avaliacao'},
            'abrigo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'abrigo_desc': ('django.db.models.fields.TextField', [], {}),
            'acesso': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'acesso_desc': ('django.db.models.fields.TextField', [], {}),
            'calcada': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'calcada_desc': ('django.db.models.fields.TextField', [], {}),
            'equipamento': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'equipamento_desc': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identificacao': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'identificacao_desc': ('django.db.models.fields.TextField', [], {}),
            'linhas': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'linhas_desc': ('django.db.models.fields.TextField', [], {}),
            'logradouro': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'logradouro_desc': ('django.db.models.fields.TextField', [], {}),
            'piso': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'piso_desc': ('django.db.models.fields.TextField', [], {}),
            'piso_tatil': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'piso_tatil_desc': ('django.db.models.fields.TextField', [], {}),
            'plataforma': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'plataforma_desc': ('django.db.models.fields.TextField', [], {}),
            'ponto': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['core.Ponto']"}),
            'rampa': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'rampa_desc': ('django.db.models.fields.TextField', [], {}),
            'transito': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'transito_desc': ('django.db.models.fields.TextField', [], {})
        },
        'core.ponto': {
            'Meta': {'object_name': 'Ponto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'nome': ('django.db.models.fields.CharField', [], {'blank': 'True', 'unique': 'True', 'max_length': '100'}),
            'osmid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'ref': ('django.db.models.fields.CharField', [], {'blank': 'True', 'unique': 'True', 'max_length': '15'})
        }
    }

    complete_apps = ['core']