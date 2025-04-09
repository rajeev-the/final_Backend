# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgentViewSet, PropertyViewSet, GeneralDataViewSet, UserDataViewSet,add_to_sheet , send_otp ,validate_otp


router = DefaultRouter()
router.register(r'agent', AgentViewSet, basename='agent')
router.register(r'property', PropertyViewSet)
router.register(r'general_data', GeneralDataViewSet)
router.register(r'users', UserDataViewSet, basename='user')  # Register UserDataViewSet
 # Register UserDataViewSet




urlpatterns = [
     path('', include(router.urls)),
     path('add-to-sheet/', add_to_sheet, name='add_to_sheet'),
     path('send-otp/',send_otp, name='send-otp'),
      path('send-otp/',validate_otp, name='validate_otp'),

]