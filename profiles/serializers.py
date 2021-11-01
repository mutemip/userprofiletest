from rest_framework import serializers
from .models import Profile, ProfileStatus


class ProfileSerialiser(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"


class ProfileAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("avartar", )


class ProfileStatusSerializer(serializers.ModelSerializer):
    user_profile = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProfileStatus
        fields = "__all__"
