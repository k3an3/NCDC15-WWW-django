# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cgi_bin', '0002_auto_20150119_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccount',
            name='user',
        ),
        migrations.DeleteModel(
            name='BankAccount',
        ),
    ]
