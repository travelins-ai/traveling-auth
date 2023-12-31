
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

from .models import UserAccount
 

 
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = UserAccount
        #fields = '__all__'
        fields = ('id', 'email', 'name',"language")
class UserAccountSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = UserAccount
        #fields = '__all__'
        fields = ('id', 'email', 'name',"has_subscription")
class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = UserAccount
        #fields = '__all__'
        fields = ('id', 'email', 'name',"language","has_subscription","customer_stripe_id")
class UserCreateMediunSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = UserAccount
        #fields = '__all__'
        fields = ('id', 'email', 'name',"language")
        
class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = UserAccount
        #fields = '__all__'
        fields = ('id', 'email', 'name')