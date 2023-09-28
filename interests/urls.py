from django.urls import path
from .views import (
    AccountInterestsUserApiView,
)

urlpatterns = [
    path('interests', AccountInterestsUserApiView.as_view())
]