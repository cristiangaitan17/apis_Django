from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import rutinas 
from .serializers import RutinaSerializer

class RutinaListView(APIView):
    def get(self, request):
        data = rutinas.objects.all()
        serializer = RutinaSerializer(data, many=True)
        return Response(serializer.data)

# Create your views here.
