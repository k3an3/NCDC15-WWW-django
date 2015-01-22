# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cgi_bin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('access_token', models.CharField(default=b'', max_length=50)),
                ('date', models.TimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
