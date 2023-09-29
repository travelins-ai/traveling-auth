from django.db import models
from accounts.models import UserAccount
from enum import Enum
# Create your models here.
class TransactionSubscription(Enum):

    FREE = "FREE"
    INITIAL_PLAN = "INITIAL"
    PROFESSIONAL_PLAN = "PROFESSIONAL"
    BUSINESS_PLAN = "BUSINESS"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)

class Subscription(models.Model):
    class Meta:
        db_table = "subscriptions"
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    subscription = models.CharField(max_length=100, choices=TransactionSubscription.choices(), default="FREE")
    subscription_id = models.CharField(max_length=150, null=True)
    next_payment = models.DateTimeField(auto_now_add=False,  null=True) 
    number_projects = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    