# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432\u043e\u043f\u0440\u043e\u0441\u0430')),
                ('answer', models.TextField(blank=True, max_length=1000, null=True, verbose_name='\u041e\u0442\u0432\u0435\u0442 \u043d\u0430 \u0432\u043e\u043f\u0440\u043e\u0441')),
                ('check', models.BooleanField(default=False, editable=False, verbose_name='\u041e\u0442\u043c\u0435\u0442\u044c\u0442\u0435 \u0433\u0430\u043b\u043e\u0447\u043a\u043e\u0439 \u0435\u0441\u043b\u0438 \u0432\u044b \u043e\u0442\u0432\u0435\u0442\u0438\u043b\u0438 \u043d\u0430 \u0432\u043e\u043f\u0440\u043e\u0441')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u0432\u043e\u043f\u0440\u043e\u0441',
                'verbose_name_plural': '\u0412\u043e\u043f\u0440\u043e\u0441\u044b',
            },
        ),
    ]