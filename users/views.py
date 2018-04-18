from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from django.http import HttpResponse,Http404
from . import models
from . import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer

from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend





class UserList(generics.ListCreateAPIView):

	queryset = User.objects.all()
	serializer_class = UserSerializer
	filter_backends = (SearchFilter,OrderingFilter)
	search_fields = ('first_name')
	ordering_fields = ('email')
	
	



class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	



# class UserList(APIView):
# 	# queryset = models.User.objects.all()
# 	# serializer_class = serializers.UserSerializer

# 	def get(self, request, format=None):
# 		users = User.objects.all()
# 		serializer = UserSerializer(users, many=True)
# 		return Response(serializer.data)

# 	def post(self, request, *args, **kwargs):
# 		serializer = UserSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	def delete(self, request, pk, format=None):
# 		user = self.get_object(pk)
# 		user.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = models.User.objects.all()
# 	serializer_class = serializers.UserSerializer
	
# 	def get_object(self, pk):
# 		try:
# 		 return User.objects.get(pk=pk)
# 		except User.DoesNotExist:
# 		 raise Http404

# 	def get(self, request, pk, format=None):
# 		user = self.get_object(pk)
# 		user = UserSerializer(user)
# 		return Response(user.data)

# 	def put(self, request, pk, format=None):
# 		user = self.get_object(pk)
# 		serializer = UserSerializer(user, data=request.DATA)
# 		if serializer.is_valid():
# 		 serializer.save()
# 		 return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	def delete(self, request, pk, format=None):
# 		user = self.get_object(pk)
# 		user.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)


