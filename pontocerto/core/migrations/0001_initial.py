# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-14 13:37
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acesso', models.CharField(choices=[('favoravel', 'Favorável'), ('aceitavel', 'Aceitável'), ('critica', 'Crítica')], max_length=10, verbose_name='Condição de Acesso')),
                ('acesso_desc', models.TextField(verbose_name='Justificativa Acesso')),
                ('abrigo', models.CharField(choices=[('favoravel', 'Favorável'), ('aceitavel', 'Aceitável'), ('critica', 'Crítica')], max_length=10, verbose_name='Condição do Abrigo')),
                ('abrigo_desc', models.TextField(verbose_name='Justificativa Abrigo')),
                ('piso', models.CharField(choices=[('favoravel', 'Favorável'), ('aceitavel', 'Aceitável'), ('critica', 'Crítica')], max_length=10, verbose_name='Condição do Piso')),
                ('piso_desc', models.TextField(verbose_name='Justificativa Piso')),
                ('rampa', models.CharField(choices=[('favoravel', 'Favorável'), ('aceitavel', 'Aceitável'), ('critica', 'Crítica')], max_length=10, verbose_name='Condição das Rampas')),
                ('rampa_desc', models.TextField(verbose_name='Justificativa Rampas')),
                ('calcada', models.CharField(choices=[('favoravel', 'Favorável'), ('aceitavel', 'Aceitável'), ('critica', 'Crítica')], max_length=10, verbose_name='Condição das Calçadas')),
                ('calcada_desc', models.TextField(verbose_name='Justificativa Calçada')),
                ('plataforma', models.CharField(choices=[('favoravel', 'Favorável'), ('aceitavel', 'Aceitável'), ('critica', 'Crítica')], max_length=10, verbose_name='Condição das Plataformas')),
                ('plataforma_desc', models.TextField(verbose_name='Justificativa Plataformas')),
                ('transito', models.CharField(choices=[('favoravel', 'Favorável'), ('aceitavel', 'Aceitável'), ('critica', 'Crítica')], max_length=10, verbose_name='Condição do Trânsito de Usuários')),
                ('transito_desc', models.TextField(verbose_name='Justificativa Trânsito')),
                ('equipamento', models.CharField(choices=[('favoravel', 'Favorável'), ('aceitavel', 'Aceitável'), ('critica', 'Crítica')], max_length=10, verbose_name='Condição dos Equipamentos')),
                ('equipamento_desc', models.TextField(verbose_name='Justificativa Equipamentos')),
                ('identificacao', models.CharField(choices=[('favoravel', 'Favorável'), ('aceitavel', 'Aceitável'), ('critica', 'Crítica')], max_length=10, verbose_name='Condição de Identificação')),
                ('identificacao_desc', models.TextField(verbose_name='Justificativa Identificação')),
                ('piso_tatil', models.CharField(choices=[('favoravel', 'Favorável'), ('aceitavel', 'Aceitável'), ('critica', 'Crítica')], max_length=10, verbose_name='Condição do Piso Tátil')),
                ('piso_tatil_desc', models.TextField(verbose_name='Justificativa Piso Tátil')),
                ('linhas', models.CharField(choices=[('favoravel', 'Favorável'), ('aceitavel', 'Aceitável'), ('critica', 'Crítica')], max_length=10, verbose_name='Condição de Identificação das Linhas de Ônibus')),
                ('linhas_desc', models.TextField(verbose_name='Justificativa Identificação das Linhas')),
                ('logradouro', models.CharField(choices=[('favoravel', 'Favorável'), ('aceitavel', 'Aceitável'), ('critica', 'Crítica')], max_length=10, verbose_name='Condição de Identificação do Logradouro')),
                ('logradouro_desc', models.TextField(verbose_name='Justificativa Logradouro')),
            ],
            options={
                'verbose_name': 'Avaliação',
                'verbose_name_plural': 'Avaliações',
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('conteudo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ponto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100)),
                ('ref', models.CharField(blank=True, max_length=15)),
                ('osmid', models.CharField(max_length=15, unique=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='ponto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Ponto'),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='ponto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Ponto'),
        ),
    ]
