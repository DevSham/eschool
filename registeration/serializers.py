# from rest_framework import serializers
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'



# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id','username', 'first_name', 'last_name', 'email')
#         extra_kwargs = {'password': {'write_only': True}}



# def create(self, validated_data):
#     user = User.objects.create_user(
#         validated_data['username'],
#         validated_data['first_name'],
#         validated_data['last_name'],
#         validated_data['email'],
#         )
#     return user



# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

 #accounts/api/serializers.py

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import serializers

User._meta.get_field('email')._unique = True


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
            )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")