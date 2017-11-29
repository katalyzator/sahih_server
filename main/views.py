# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from main.models import Question


@csrf_exempt
def get_question(request):
    try:
        username = request.POST.get('username')
        question = request.POST.get('question')

        question_object = Question()

        question_object.title = question
        question_object.username = username
        question_object.save()

        return JsonResponse(dict(result=True))
    except:
        return JsonResponse(dict(result=False))
