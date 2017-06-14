from django.shortcuts import render
from rest_framework import viewsets
from shelf.serializers import AuthorSerializer, BookSerializer
from shelf.models import Book, Author
import pdb;

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()