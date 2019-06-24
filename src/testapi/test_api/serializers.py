from rest_framework import serializers
from . import  models

class HelloSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):

        user = models.UserProfile(
            name = validated_data['name'],
            email = validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class ProfileFeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProfileFeedItem
        fields = {'id', 'user_profile', 'status_text', 'created_on'}
        extra_kwargs = {'user_profile': {'read_only': True}}