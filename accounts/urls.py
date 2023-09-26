
from django.urls import path
from .views import (
     index,
     
)

urlpatterns = [ 
   path("accounts/google", index, name="index"),
]
