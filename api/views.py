from rest_framework import viewsets
from .models import Agent, Property, GeneralData ,UserData
from .serializers import AgentSerializer, PropertySerializer, GeneralDataSerializer,UserDataSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

from google.oauth2 import service_account
import os
from googleapiclient.discovery import build
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

import requests

# from rest_framework.decorators import api_view








# Setup of googleSheet API


# Path to your service account key file
SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), './corded-reality-454716-c5-3070ca6255e4.json')
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Initialize the Google Sheets API client
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    @action(detail=False, methods=['get'], url_path="search-by-phone")
    def search_by_phone(self, request):
        phone = request.query_params.get('phone', None)
        if phone:
            agent = Agent.objects.filter(phone_number=phone).first()
            if agent:
                serializer = self.get_serializer(agent)
                return Response({"exists": True, "agent": serializer.data})
            else:
                return Response({"exists": False}, status=404)
        return Response({"error": "Phone number is required"}, status=400)


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        SPREADSHEET_ID = "106keBTXZC4OONim_jyvEQIGtoKKNh4eAFWU0mLtZn_0"

        # Extract the data from the response
        property_data = response.data


        # Prepare the row to be inserted into the Google Sheet
        row = [
            property_data.get("state", ""),
            property_data.get("address", ""),
            property_data.get("acre_price", ""),
            property_data.get("acre", ""),
            property_data.get("available", ""),
            property_data.get("road_width", ""),
            property_data.get("land_category", ""),
            property_data.get("district_name", ""),
            property_data.get("tehsil_name", ""),
            property_data.get("locations_link", ""),
            property_data.get("img", ""),
            property_data.get("agent", ""),
        ]

        # Define the range where the data will be inserted
        range_name="Sheet1!A1" # Use full sheet name instead of specific cell range

        # Create the request body
        body = {
            "values": [row]
        }

        try:
            # Insert the data into the sheet
            service.spreadsheets().values().append(
                spreadsheetId=SPREADSHEET_ID,
                range=range_name,
                valueInputOption="RAW",
                body=body,
            ).execute()
        except Exception as e:
            print(f"Error inserting data into Google Sheet: {e}")

        return response

class GeneralDataViewSet(viewsets.ModelViewSet):
    queryset = GeneralData.objects.all()
    serializer_class = GeneralDataSerializer




class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer

    @action(detail=False, methods=['get'], url_path="search-by-phone")
    def search_by_phone(self, request):
        phone = request.query_params.get("phone", None)  # Use query parameters
        if phone:
            user = UserData.objects.filter(phone=phone).first()
            if user:
                serializer = self.get_serializer(user)
                return Response({"exists": True, "user": serializer.data})
            else:
                return Response({"exists": False}, status=404)
        return Response({"error": "Phone number is required"}, status=400)


  # Remove CSRF protection for simplicity
@csrf_exempt
def add_to_sheet(request):
    if request.method == "POST":
        data = json.loads(request.body)
        SPREADSHEET_ID ="1zr_aupoOV_ioVHqRkdw2za7AMU7SNzuPbniD__nBz2E"

        # Insert data into Google Sheet
        row =[
            data.get("phone_User", ""),
            data.get("User_name", ""),
            data.get("Agent_name", ""),
            data.get("phone_Agent", "")
        ]
         # Define the range where the data will be inserted
        range_name = 'Sheet1!A1:F1'  # Adjust the range as needed

        # Create the request body
        body = {
            'values': [row]
        }

        try:
            # Insert the data into the sheet
            service.spreadsheets().values().append(
                spreadsheetId=SPREADSHEET_ID,
                range=range_name,
                valueInputOption='RAW',
                body=body
            ).execute()
        except Exception as e:
            # Log the error or handle it as needed
            print(f"Error inserting data into Google Sheet: {e}")

        return JsonResponse({"message": "Data inserted successfully"}, status=201)




@csrf_exempt
def send_otp(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body.decode('utf-8'))
            phone = body.get('phone')

            if not phone:
                return JsonResponse({'error': 'Phone number is required'}, status=400)

            # Replace with your actual authToken (consider storing this in environment vars or settings.py)
            auth_token = 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJDLTMxODFCMTBGRDBFQTRDQyIsImlhdCI6MTc0NDEzOTI5MiwiZXhwIjoxOTAxODE5MjkyfQ.72rcAm8qCWPnjilr88SJx-HbFjf8pe6cEPOyZrBXADHu97cjVFKFhyZ2BqdJXNAu87U4HRvx6ar1ATgF7D50pA'

            # Construct the API URL with query parameters
            url = f"https://cpaas.messagecentral.com/verification/v3/send?countryCode=91&customerId=C-3181B10FD0EA4CC&flowType=SMS&mobileNumber={phone}"

            headers = {
                'authToken': auth_token
            }

            response = requests.post(url, headers=headers)

            print("📨 MessageCentral Response:", response.status_code, response.text)

            return JsonResponse(response.json(), status=response.status_code)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Only POST method allowed'}, status=405)






@csrf_exempt
def validate_otp(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body.decode('utf-8'))

            phone = body.get('phone')
            verification_id = body.get('verificationId')
            otp_code = body.get('code')

            if not phone or not verification_id or not otp_code:
                return JsonResponse({'error': 'Phone, verificationId, and code are required'}, status=400)

            # Replace with your actual authToken (secure it in settings/env)
            auth_token = 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJDLTMxODFCMTBGRDBFQTRDQyIsImlhdCI6MTc0NDEzOTI5MiwiZXhwIjoxOTAxODE5MjkyfQ.72rcAm8qCWPnjilr88SJx-HbFjf8pe6cEPOyZrBXADHu97cjVFKFhyZ2BqdJXNAu87U4HRvx6ar1ATgF7D50pA'

            # Create the validation URL
            url = (
                f"https://cpaas.messagecentral.com/verification/v3/validateOtp"
                f"?countryCode=91"
                f"&mobileNumber={phone}"
                f"&verificationId={verification_id}"
                f"&customerId=C-3181B10FD0EA4CC"
                f"&code={otp_code}"
            )

            headers = {
                'authToken': auth_token
            }

            response = requests.get(url, headers=headers)

            print("✅ MessageCentral OTP Validate Response:", response.status_code, response.text)

            return JsonResponse(response.json(), status=response.status_code)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Only POST method allowed'}, status=405)


