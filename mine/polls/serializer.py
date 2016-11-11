from django.contrib.auth.models import User
from polls.models import Question,Stat
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_text','pu_date','id','status')



class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stat
        fields=('category_count',)
