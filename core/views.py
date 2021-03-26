from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from django.contrib.auth.models import User

from .models import Book
from .serializers import (
                          BookSerializer,
                          RegistrationSerializer 
                          )
    
    
class BookCreateView(generics.CreateAPIView):
    """Create a Book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookListView(generics.ListAPIView):
    """Show all books"""
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        user = self.request.user
        return Book.objects.filter(user=user)


class BookDetailView(generics.RetrieveAPIView):
    """Show detail of the book"""
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        user = self.request.user
        return Book.objects.filter(user=user)
    

class BookUpdateView(generics.RetrieveUpdateDestroyAPIView):
    """update detail of the book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)
    
    
    def delete(self, request, *args, **kwargs):
        book = Book.objects.filter(user=self.request.user, pk=kwargs['pk'])
        if book.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('Book is not yours!')
    
    def perform_update(self, serializer, **kwargs):
        book = Book.objects.get(pk=self.kwargs['pk'])
        if self.request.user != book.user:
            raise ValidationError("You are not the owner of this book")
        serializer.save(user=self.request.user, book=book)
    

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]