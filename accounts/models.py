from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone 

# Create your models here.
class UserAccountManager(BaseUserManager):
    def create_user(self, email, name=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        
        if  name is None:
            user = self.model(email=email, name=email.split('@')[0])
        else:
            user = self.model(email=email, name=name)
        user.set_password(password)
    
        user.save()
        
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = "accounts"  
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    has_subscription = models.BooleanField(default=False)
    language = models.CharField(max_length=2,default="es")
    customer_stripe_id = models.CharField(max_length=100, null=True, blank=True)
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.name
    
    def __str__(self):
        return self.email