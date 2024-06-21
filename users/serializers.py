from rest_framework import serializers

from users.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        new_user = User.objects.create_user(**validated_data)
        return new_user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = User.objects.filter(email=data['email']).first()
        if not user:
            raise serializers.ValidationError({"email": "Wrong credentials or user is not registered yet"})
        if not user.check_password(data['password']):
            raise serializers.ValidationError({"password": "Password is not correct"})

        data['user'] = user

        return data


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)
        read_only_fields = ('email',)
