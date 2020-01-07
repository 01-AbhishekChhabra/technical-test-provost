from django.db import transaction
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny

from drivers.models import Drivers
from booking_requests.models import Booking_Requests
from riders.models import Riders
import json

SUCCESS_STATUS = status.HTTP_200_OK
ERROR_STATUS   = status.HTTP_400_BAD_REQUEST

class AddDummyData(generics.CreateAPIView):
    parser_classes = MultiPartParser,
    permission_classes = (AllowAny,)

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        print(request.body)
        request.body = json.loads(request.body)
        print(request.body.get('filePath'))

        filePath = request.body.get('filePath')
        # filePath = '../data.json'
        try:
            with open(filePath) as json_file:
                data = json.load(json_file)
        except Exception as e:
            response = {
                'message': str(e)
            }
            return Response(response, ERROR_STATUS)
        
        # drivers array in data
        # booking_request array in data

        drivers = data['drivers']

        for index in range(0, len(drivers)):
            driver = Drivers()
            try:
                driver.name = drivers[index].get('name')
                driver.id = drivers[index].get('id')
            except:
                response = {
                    'success': False
                }
                return Response(response, ERROR_STATUS)
            driver.save()
        
        booking_requests = data['booking_requests']

        for index in range(0, len(booking_requests)):
            rider = Riders()
            try:
                rider.name = booking_requests[index].get('rider_name')
            except: 
                response = {
                    'success': False
                }
                return Response(response, ERROR_STATUS)
            rider.save()
            

        for index in range(0, len(booking_requests)):
            
            booking_request = Booking_Requests()
            try:

                booking_request.rider_name = booking_requests[index].get('rider_name')
                booking_request.from_location = booking_requests[index].get('from_location')
                booking_request.to_location = booking_requests[index].get('to_location')
                

                if booking_requests[index].get('driver') != None:
                    driver = Drivers.objects.get(id = booking_requests[index].get('driver'))
                    booking_request.driver = driver


                booking_request.timestamp = booking_requests[index].get('timestamp')
            except: 
                response = {
                    'success': False
                }
                return Response(response, ERROR_STATUS)

            booking_request.save()

        response = {
            'success' : True
        }

        return Response(response, SUCCESS_STATUS)


        