from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    '''
    UserSerializer Class for the user model
    '''
    username = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(max_length=100, required=True)
    email = serializers.EmailField(max_length=100, required=True)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        '''
        Create and return a new `User` instance, given the validated data.
        '''
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        '''
        Update and return an existing `User` instance, given the validated data.
        '''
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance