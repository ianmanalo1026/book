from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from .models import Book, Upvote
from .serializers import (
                          BookSerializer, 
                          UpvoteSerializer, 
                          RegistrationSerializer
                          )


class UserRegisterationView(generics.CreateAPIView):
    """Create new user that generate automatic token"""
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user).key
            data = {'token':token}
        else:
            data = serializer.errors
        return Response(data=data, status=201)
    
    
class LoginView(generics.CreateAPIView):
    serializer_class = AuthTokenSerializer
    
    def create(self, request):
        return ObtainAuthToken().as_view()(request=request._request)
    
    
class BookCreateView(generics.CreateAPIView):
    """Create a Book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookListView(generics.ListAPIView):
    """Show all books"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookDetailView(generics.RetrieveAPIView):
    """Show detail of the book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    

class BookUpdateView(generics.RetrieveUpdateDestroyAPIView):
    """update detail of the book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    
    
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
    
    
class UpvoteCreateView(generics.CreateAPIView):
    """Vote for a specific book"""
    serializer_class = UpvoteSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        book = Book.objects.get(pk=self.kwargs['pk'])
        return Upvote.objects.filter(user=user, book=book)
    
    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('You have already voted on this!')
        user = self.request.user
        book = Book.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=user, book=book)
