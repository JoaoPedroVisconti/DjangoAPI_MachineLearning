from dataclasses import field
from rest_framework import serializers
from .models import Candidature


class CandidatureSerializers(serializers.ModelSerializer):
  class Meta:
    model = Candidature
    fields = '__all__'
