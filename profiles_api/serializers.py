from rest_framework.serializers import Serializer, CharField, ModelSerializer

from profiles_api.models import UserProfile


class HelloSerializer(Serializer):
    """Serializes a name field for testing our APIView"""
    name = CharField(max_length=10)


class UserProfileSerializer(ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }}

        def create(self, validated_data):
            """Create and return a new user"""
            user = UserProfile.objects.create_user(
                email=validated_data['email'],
                name=validated_data['name'],
                password=validated_data['password'],
            )
            return user
