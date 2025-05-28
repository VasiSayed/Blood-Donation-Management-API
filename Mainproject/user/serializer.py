from rest_framework import serializers
from .models import Donation,Patient,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields='__all__'


class DonatioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donation
        fields='__all__'