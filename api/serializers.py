from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields =['id', 'username', 'tasks']
