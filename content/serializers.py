from rest_framework import serializers
from .models import BlogPost, News, Contact


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'created_at']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'content', 'created_at']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'consultation_type', 'message']
