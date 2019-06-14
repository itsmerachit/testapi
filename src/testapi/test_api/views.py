from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from rest_framework import status

# Create your views here.

class HelloApiView(APIView):

    def get(request, format=None):
        api_view = [
            'hello',
            'second line',
            'third line'
        ]
        return Response({'message': 'Hello', 'api_view': api_view})

    serializer_class = serializers.HelloSerializer

    def post(self, request):
        serializer = serializers.HelloSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'hello {0}'.format(name)
            return Response({'name': name, 'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request):
        return Response({'method':'patch'})

    def put(self,request):
        return Response({'method':'put'})

    def delete(self,request):
        return Response({'method': 'delete'})