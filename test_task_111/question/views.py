from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ViewSet, ReadOnlyModelViewSet
from .models import Question, QuestionNumber
from .serializers import QuestionSerializer
from .utils import get_requests_question
from rest_framework.response import Response
from rest_framework import status


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filterset_fields = ['id', 'question_id', 'question', 'answer', 'time_create']

class QuestionForNumberViewSet(ViewSet):
    queryset = QuestionNumber.objects.all()

    def create(self, request):
        """
        :param request: {"questions_num": integer}
        :return:
        """
        request_value = request.data.get("questions_num")
        if str(request_value).isdigit():
            for i in range(int(request_value)+1):
                while True:
                    data = get_requests_question(1)
                    if Question.objects.filter(question_id=data[0]['id']).last() != data[0]['id']:
                        queryset_data = Question.objects.create(question_id=data[0]['id'], question=data[0]['question'],
                                                                answer=data[0]['answer'], time_create=data[0]['created_at'])
                        queryset_data.save()
                        break
                    else:
                        continue
            toresponse = QuestionSerializer(Question.objects.all().last())
            return Response(status=status.HTTP_201_CREATED, data=toresponse.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


