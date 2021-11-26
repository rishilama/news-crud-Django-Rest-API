from django.db.models import fields
from rest_framework import serializers
from . models import News

class NewsViewSet(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        