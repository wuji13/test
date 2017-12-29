# -*- coding:utf-8 -*-
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = ('id', 'title', 'description', 'completed', 'create_date')