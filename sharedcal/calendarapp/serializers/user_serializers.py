from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'password'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        email = validated_data.get('email')
        username = validated_data.get('username')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        password = validated_data.get('password')

        user = get_user_model()
        new_user = user.objects.create(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name
        )

        new_user.set_password(password)
        new_user.save()

        return new_user