from rest_framework import serializers
from .models import User
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password', 'email')