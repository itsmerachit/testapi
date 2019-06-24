from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import viewsets
from . import serializers
from rest_framework import status
from . import models, permissions
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
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


class HelloViewsets(viewsets.ViewSet):


    def list(self, request):
        some_viewset = [
            'This is api viewset',
            'accessing using router class'
        ]
        return Response({'Title': 'Hello', 'message': some_viewset})


    serializer_class = serializers.HelloSerializer


    def create(self, request):

        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'hello {0}'.format(name)
            return Response({'name': name, 'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request):
        return Response({'Method':'Put'})


    def partial_update(self, request):
        return Response({'Method':'Patch'})


    def retrieve(self, request):
        return Response({'Method':'Get'})


    def delete(self, request):
        return Response({'Method':'Delete'})


class UserProfileViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):

    serializer_class = AuthTokenSerializer

    def create(self, request):
        return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)


    def perform_create(self, serializer):
        serializer.save(user_profile = self.request.user)
