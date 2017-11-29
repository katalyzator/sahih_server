# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_unicode


class Question(models.Model):
    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'Вопросы'

    username = models.CharField(max_length=255, verbose_name='Username')
    title = models.CharField(max_length=1000, verbose_name='Название вопроса')
    answer = models.TextField(max_length=1000, verbose_name='Ответ на вопрос', blank=True, null=True)

    check = models.BooleanField(default=False, verbose_name='Отметьте галочкой если вы ответили на вопрос',
                                editable=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.title)

    def save(self, *args, **kwargs):
        if self.answer:
            self.check = True

        super(Question, self).save(*args, **kwargs)
