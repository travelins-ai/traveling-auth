from rest_framework import serializers
from subscriptions.models import TransactionSubscription

from subscriptions.models import Subscription
 

class SubscriptionModelSerializer(serializers.ModelSerializer):
    subscription = serializers.ChoiceField(choices=TransactionSubscription.choices())

    class Meta:
        model = Subscription
        fields = '__all__'
