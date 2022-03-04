from django.db import models

from django.contrib.auth.models import (
    BaseUserManager,AbstractBaseUser
)
#from django.contrib.auth.models import User

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None ):
        """Create and Save a user with email and password"""
        if not email:
            raise ValueError("User must have email address")

        #domain part of email is lowercase.
        email = self.normalize_email(email)
        user = self.model(email=email, date_of_birth=date_of_birth)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,date_of_birth, password=None):
        """Create and Save a superuser with email and password"""
        user = self.create_user(email, password=password, date_of_birth=date_of_birth)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True)
    date_of_birth = models.DateField()
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self, app_label):
        return True

class Profile(models.Model):
    GENDER_CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user_profile')
    full_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=50)
    description = models.TextField()
    date_of_join = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE, default="Male")
    profile_image = models.ImageField(upload_to = 'profile/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

