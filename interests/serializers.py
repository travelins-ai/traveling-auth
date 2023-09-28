from rest_framework import serializers

from interests.models import AccountInterests


 

class AccountInterestsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountInterests
        fields = '__all__'
