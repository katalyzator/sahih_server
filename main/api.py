from tastypie.resources import ModelResource

from main.models import Question

api_object_question = Question.objects.filter(check=True)


class QuestionResource(ModelResource):
    class Meta:
        queryset = api_object_question
        name = 'question'
        limit = 1000
