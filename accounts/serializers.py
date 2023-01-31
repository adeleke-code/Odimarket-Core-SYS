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
	def	save(self):
		account = User(
					first_name=self.validated_data['first_name'],
                    last_name=self.validated_data['last_name'],
					email=self.validated_data['email'],
                    phone=self.validated_data['phone']
				)
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		if password != password2:
			raise serializers.ValidationError({'password': 'Passwords must match.'})
		account.set_password(password)
		account.save()

		return account






class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=700)
    password = serializers.CharField(max_length=700)

