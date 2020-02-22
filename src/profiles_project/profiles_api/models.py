from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """helps django work with our custom user model"""

    def create_user(self , email , name , password = None):
        """create a new user profile object"""

        if not email:
            raise ValueError("user must have a email adress")

        email = self.normalize_email(email)
        user = self.model(email = email , name = name)

        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self , email , name , password):
        """"create and save a new super user with given details"""

        user = self.create_user(email , name , password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using = self._db)

        return user

class UserProfile(AbstractBaseUser , PermissionsMixin):
    """Represents a user proflie inside our system"""

    email = models.EmailField(max_length = 255 , unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = UserProfileManager()                                 # manages user proflie required when substituting in django custom user model

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']                                     # email already set to a required fiel in the above line

    def get_full_name(self):
        """Used to get the users full name"""

        return self.name

    def get_short_name(self):
        """used to get users short name"""

        return self.name

    def __str__(self):
        """django uses this when it needs to convert the object to a string"""

        return self.email
