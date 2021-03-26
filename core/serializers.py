from rest_framework import serializers
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
        