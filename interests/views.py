from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from interests.models import AccountInterests
from interests.serializers import AccountInterestsModelSerializer
# Create your views here.

listRequiredIntests= ['DESTINATION_TYPE','TRAVEL_RHYTHM','COMFORT_OR_BUDGET','RESTRICTION','FOOD_PREFERENCE','REQUIREMENTS']


class AccountInterestsUserApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, user_id):
        '''
        Helper method to get the object with given userid
        '''
        try:
            return AccountInterests.objects.filter(user=user_id)
        except AccountInterests.DoesNotExist:
            return None

    def get(self, request,  *args, **kwargs):
        '''
        Retrieves the AccountInterests with given todo_id
        '''
        provider_instance = self.get_object(request.user.id)
        if not provider_instance:
            return Response(
                {"message": "Object with interests from user session does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = AccountInterestsModelSerializer(provider_instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request):
        
        '''
        Create a new invitation for the given user
        ''' 

        if not request.data:
            return Response(
                {"message": "data is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if not request.data['interest_type_key'] in listRequiredIntests:
            return Response(
                {"message": "incorrect supplied value in interest_type_key"},
                status=status.HTTP_400_BAD_REQUEST
            ) 
        request.data['user'] = request.user.id
        serializer = AccountInterestsModelSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save() 
            return Response({
                "message":f'add record interest: {serializer.data["id"]}'
                }, status=status.HTTP_201_CREATED) 
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    
    