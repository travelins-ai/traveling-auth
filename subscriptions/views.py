from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from subscriptions.models import Subscription
from subscriptions.serializers import SubscriptionModelSerializer
from accounts.models import  UserAccount
from travelingAuths.core.services.subscription_services import created_subscription
# Create your views here.
class SubscriptionUserApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, user_id):
        '''
        Helper method to get the object with given userid
        '''
        try:
            return Subscription.objects.get(user=user_id)
        except Subscription.DoesNotExist:
            return None

    def get(self, request,  *args, **kwargs):
        '''
        Retrieves the Provider with given todo_id
        '''
        subscription = self.get_object(request.user.id)
        if not subscription:
            new_subscription = created_subscription(request.user.id)
            if  new_subscription is None:
                return Response(
                    {"message": "Error creating subscription"},
                    status=status.HTTP_400_BAD_REQUEST
                ) 
            return Response(new_subscription, status=status.HTTP_200_OK)

        serializer = SubscriptionModelSerializer(subscription)
        return Response(serializer.data, status=status.HTTP_200_OK)