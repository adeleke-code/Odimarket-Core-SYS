from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'password', 'password2']
        extra_kwargs = {
				'password': {'write_only': True},
		}	

    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.pop('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password Does not match")
        return attrs
    
    def create(self, validate_data):

        return User.objects.create_user(**validate_data)

	

class ArtisanRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'password', 'password2']
        extra_kwargs = {
				'password': {'write_only': True},
		}	

    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.pop('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password Does not match")
        return attrs
    
    def create(self, validate_data):

        return User.objects.create_artisan(**validate_data)






class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=700)
    password = serializers.CharField(max_length=700)

