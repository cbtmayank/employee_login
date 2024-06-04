from rest_framework import serializers
from .models import cbtUser

class loginAppSerializer(serializers.ModelSerializer):

    class Meta:
        model = cbtUser
        fields = ("__all__")