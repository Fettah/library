from rest_framework import serializers
from shelf.models import Author, Book, Tag
import pdb
class BookSerializer(serializers.HyperlinkedModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ('id', 'title', 'published_at', 'author_id')

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('url', 'id', 'first_name', 'last_name', 'books' )

    def create(self, validated_data):
        books = validated_data.pop('boooks')
        author = Author.objects.create(**validated_data)
        return author


class TagsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')