from polls.models import Question,Stat
from rest_framework import viewsets
from .serializer import QuestionSerializer,StatSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('pu_date')
    serializer_class = QuestionSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        if Stat.objects.exists():
            s = Stat.objects.get()
            s.category_count +=1
            s.save()
        else:
            Stat.objects.create(category_count=1)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def change_status(self,request,*args,**kwargs):
        instance = self.get_object()
        
        instance.status = 0
        instance.save()
        s= Stat.objects.get()
        s.category_count -=1
        s.save()
        return Response("DELETED")

    def get_queryset(self):
        q=Question.objects.filter(status=1)
        return(q)


class StatView(viewsets.ModelViewSet):
    queryset=Stat.objects.all()
    serializer_class=StatSerializer


class RandomView(APIView):

    def get(self,request):
        dic={"abcd":123,"efg":456}
        return Response(dic)
