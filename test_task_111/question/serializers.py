
from rest_framework import serializers
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Question
        fields = '__all__'

