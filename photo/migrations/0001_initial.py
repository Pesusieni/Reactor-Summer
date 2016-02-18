# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=25)),
                ('description', models.TextField(blank=True, null=True)),
                ('uploader', models.CharField(max_length=25)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='photos/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nick_name', models.CharField(max_length=20)),
                ('reply', models.TextField(max_length=400)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ForeignKey(to='photo.Photo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='photo',
            name='tags',
            field=models.ManyToManyField(to='photo.Tag'),
            preserve_default=True,
        ),
    ]
