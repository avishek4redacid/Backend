from django.contrib.auth.models import User

from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'first_name', 'last_name', 'company_name', 'city','state', 'zip_code', 'email', 'web','age',)
        model = models.User
        