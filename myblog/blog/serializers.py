# -*- coding:utf-8 -*-
from rest_framework import serializers
from models import article


#Serializer是将「Model序列化」，且一一对应,需要继承serializers.ModelSerializer， fields为API想要得到的字段。

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = article
        fields = ('id', 'title', 'content')