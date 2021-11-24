from rest_framework.viewsets import ModelViewSet
from user.models import CustomUser, UserProfile
from user.serializers import UserProfileSerializer, CustomUserSerializer

# Create your views here.
class CustomUserView(ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

class UserProfileView(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
