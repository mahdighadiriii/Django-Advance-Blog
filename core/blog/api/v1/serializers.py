from rest_framework import serializers
from ...models import Post, Category




class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):

    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content','snippet','category', 'status', 'relative_url', 'created_date', 'published_date']

    

