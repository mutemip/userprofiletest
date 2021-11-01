from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Profile
from serializers import ProfileSerialiser

class ProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerialiser
    permission_classes = [IsAuthenticated]