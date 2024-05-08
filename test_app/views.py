from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from .models import Register1

from .models import Test,User
from .serializers import TestSerializer, UserSerializer, ResultSerializer

class TestView(APIView):
    def get(self, request: Request, pk=None,q_type=None,q_subject=None) -> Response:
        if pk is None and q_subject is None and q_type is None:
            tests = Test.objects.all()
            serializer = TestSerializer(tests, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif q_subject==None and q_type==None:
            try:
                test = Test.objects.get(pk=pk)
                serializer = TestSerializer(test)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Test.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        elif pk==None and q_subject==None:
            try:
                test = Test.objects.filter(question_type1=q_type)
                serializer = TestSerializer(test,many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Test.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        elif pk==None:
            try:
                task = Test.objects.filter(question_type1=q_type,question_subject=q_subject)
                serializer = TestSerializer(task,many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Test.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
from django.http import JsonResponse
from .models import Register1
from .serializers import RegisterSerializer

def register(request):
    if request.method == 'GET':
        registers = Register1.objects.all()
        serializer = RegisterSerializer(registers, many=True)
        return JsonResponse(serializer.data, safe=False)
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def login(request):
    uname = request.data.get('uname')
    password = request.data.get('password')
    # Bu erda foydalanuvchi autentifikatsiyasi uchun kerakli logika yoziladi
    # Misol uchun, foydalanuvchi ma'lumotlari tekshiriladi va to'g'ri bo'lsa autentifikatsiya muvaffaqiyatli deb qaytariladi
    if uname == 'test' and password == 'test123':
        return Response({'status': 'auth'})
    else:
        return Response({'status': 'invalid'})