from django.db import models
from django.db.models import fields
from rest_framework import serializers
from classifier.models import Image


class ImageSerializer(serializers.ModelSerializer):

    ans_class = serializers.ReadOnlyField()
    score = serializers.ReadOnlyField()
    
    class Meta:
        model = Image
        fields = ['id','title','image','ans_class','score']
