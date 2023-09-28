from django.db import models
from enum import Enum
# Create your models here.
from accounts.models import UserAccount
class TransactionInterest(Enum):

    DESTINATION_TYPE = "DESTINATION_TYPE"
    TRAVEL_RHYTHM = "TRAVEL_RHYTHM"
    COMFORT_OR_BUDGET = "COMFORT_OR_BUDGET"
    RESTRICTION = "RESTRICTION"
    FOOD_PREFERENCE = "FOOD_PREFERENCE"
    REQUIREMENTS = "REQUIREMENTS"
    
    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class AccountInterests(models.Model):
    class Meta:
        db_table = "interests"
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    interest_type_key = models.CharField(max_length=100, choices=TransactionInterest.choices(), null=False)
    interest_type_value = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)