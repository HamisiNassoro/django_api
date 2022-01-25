from rest_framework.viewsets import ModelViewSet
from user.models import CustomUser, UserProfile
from user.serializers import UserProfileSerializer, CustomUserSerializer
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
import pyotp
from rest_framework.response import Response
from rest_framework.views import APIView
import base64

# Create your views here.
class CustomUserView(ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.prefetch_related("user_profile","user_profile__address_info") #for a reverse relationship we use prefetch related

class UserProfileView(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.select_related("user", "address_info") #for a direct relationship we use select_related



# This class returns the string needed to generate the key
class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + "Some Random Secret Key"

class getPhoneNumberRegistered(APIView):
    # Get to Create a call for OTP
    @staticmethod
    def get(request, phone):
        try:
            mobile = CustomUser.objects.get(mobile=phone)  # if Mobile already exists the take this else create New One
        except ObjectDoesNotExist:
            CustomUser.objects.create(
                mobile=phone,
            )
            mobile = CustomUser.objects.get(mobile=phone)  # user Newly created Model

        mobile.counter += 1  # Update Counter At every Call
        mobile.save()  # Save the data
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
        OTP = pyotp.HOTP(key)  # HOTP Model for OTP is created
        print(OTP.at(mobile.counter))
        # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
        return Response({"OTP": OTP.at(mobile.counter)}, status=200)  # Just for demonstration


    # This Method verifies the OTP
    @staticmethod
    def post(request, phone):
        try:
            mobile = CustomUser.objects.get(mobile=phone)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
        OTP = pyotp.HOTP(key)  # HOTP Model
        if OTP.verify(request.data["otp"], mobile.counter):  # Verifying the OTP
            mobile.isVerified = True
            mobile.save()
            return Response("You are authorised", status=200)
        return Response("OTP is wrong", status=400)


# Time after which OTP will expire
EXPIRY_TIME = 50 # seconds

class getPhoneNumberRegistered_TimeBased(APIView):
    # Get to Create a call for OTP
    @staticmethod
    def get(request, phone):
        try:
            mobile = CustomUser.objects.get(mobile=phone)  # if Mobile already exists the take this else create New One
        except ObjectDoesNotExist:
            CustomUser.objects.create(
                mobile=phone,
            )
            mobile = CustomUser.objects.get(mobile=phone)  # user Newly created Model
        mobile.save()  # Save the data
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
        OTP = pyotp.TOTP(key,interval = EXPIRY_TIME)  # TOTP Model for OTP is created
        print(OTP.now())
        # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
        return Response({"OTP": OTP.now()}, status=200)  # Just for demonstration

    
    # This Method verifies the OTP
    @staticmethod
    def post(request, phone):
        try:
            mobile = CustomUser.objects.get(mobile=phone)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
        OTP = pyotp.TOTP(key,interval = EXPIRY_TIME)  # TOTP Model 
        if OTP.verify(request.data["otp"]):  # Verifying the OTP
            mobile.isVerified = True
            mobile.save()
            return Response("You are authorised", status=200)
        return Response("OTP is wrong/expired", status=400)
