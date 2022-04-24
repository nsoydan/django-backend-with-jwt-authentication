from email import message
from sys import breakpointhook
from telnetlib import STATUS
from django.http import Http404, HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Bakim_List
from boApp.serializers import BakimSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class TodoView(APIView):
    permission_classes=[IsAuthenticated]
    
    
    def get(self,request):        
        todos = Bakim_List.objects.all()
        serializer = BakimSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self,request):
        print("Buraya kadar geldi.....")
        data = JSONParser().parse(request)
        serializer = BakimSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)    


class TodoDetailsView(APIView):
    permission_classes=[IsAuthenticated]
    def getObject(self,pk):
        try:
            return Bakim_List.objects.get(pk=pk)
        except Bakim_List.DoesNotExist:
            raise Http404
    
    def get(self,request,pk):
        print("todo details get içinde")
        todo=self.getObject(pk)
        serializer= BakimSerializer(todo)
        return JsonResponse(serializer.data)
    
    def put(self,request,pk):
        
        todo=self.getObject(pk)
        data=JSONParser().parse(request)
        serializer=BakimSerializer(todo,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.data,status=400)

    def delete(self,request,pk):
        print("delete in içinde")
        todo=self.getObject(pk)
        todo.delete()
        return HttpResponse(status=204)
