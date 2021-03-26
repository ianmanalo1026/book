from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """Serializer for Book"""
    
    class Meta:
        model = Book
        fields = (
            'id','user',
            'title', 'author',
            'description', 'image')
        read_only_fields = ('id', 'user')
        
        
class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        
    def create(self, validated_data):
        user = User.objects.create(
                                   username=validated_data['username'],
                                   email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user