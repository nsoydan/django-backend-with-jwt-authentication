from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
# Create your views here.
from django.shortcuts import render,redirect
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate,login,logout

from accounts.serializers import AccountSerializer
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

def login_view(request):
    
    return HttpResponse('<h3>Login_view çalıştı</h3>')

def logout_view(request):
    logout(request)
    return redirect('/')

class UserView(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self,request):
        users = User.objects.all()
        serializer = AccountSerializer(users, many=True)
        return Response(serializer.data)

    def post(self,request):
        
        data = JSONParser().parse(request)
        serializer = AccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def details(request,pk):
    try:
        user=User.objects.get(username=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer= AccountSerializer(user)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data=JSONParser().parse(request)
        serializer=AccountSerializer(user,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.data,status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)
