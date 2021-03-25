from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Upvote

class BookSerializer(serializers.ModelSerializer):
    """Serializer for Book"""
    upvotes = serializers.SerializerMethodField()
    
    def get_upvotes(self, book):
        return Upvote.objects.filter(book=book).count()
    
    class Meta:
        model = Book
        fields = (
            'id','user',
            'title', 'author',
            'description', 'image', 'upvotes' )
        read_only_fields = ('id', 'user')
        
        
class UpvoteSerializer(serializers.ModelSerializer):
    """Serializer for upcote"""
    class Meta:
        model = Upvote
        fields = ('id',)
        read_only_fields = ('id',)
        

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input type':'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user