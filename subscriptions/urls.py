from django.urls import path
from .views import (
    SubscriptionUserApiView,
)
urlpatterns = [
    path('subscriptions', SubscriptionUserApiView.as_view())
]