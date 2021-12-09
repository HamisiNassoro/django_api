from rest_framework.viewsets import ModelViewSet
from user.models import CustomUser, UserProfile
from user.serializers import UserProfileSerializer, CustomUserSerializer

# Create your views here.
class CustomUserView(ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.prefetch_related("user_profile","user_profile__address_info") #for a reverse relationship we use prefetch related

class UserProfileView(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.select_related("user", "address_info") #for a direct relationship we use select_related
