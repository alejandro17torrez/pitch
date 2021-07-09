from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import Enclosure

class EnclosureSerializer(ModelSerializer):
    class Meta:
        model = Enclosure
        fields = '__all__'

