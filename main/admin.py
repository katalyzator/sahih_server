# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from main.models import Question


class QuestionAdmin(admin.ModelAdmin):
    class Meta:
        model = Question


admin.site.register(Question, QuestionAdmin)
