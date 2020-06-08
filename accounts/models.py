from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, full_name=None, password=None, is_active=True, is_staff=False,is_Agent=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            email = self.normalize_email(email),
            full_name=full_name
        )
        user_obj.set_password(password) # change user password
        user_obj.staff = is_staff
        user_obj.Agent = is_Agent
        user_obj.admin = is_admin
        user_obj.is_active= is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email,full_name=None, password=None):
        user = self.create_user(
                email,
                full_name=full_name,
                password=password,
                is_staff=True
        )
        return user

    def create_Agentuser(self, email,full_name=None, password=None):
        user = self.create_user(
                email,
                full_name=full_name,
                password=password,
                is_Agent=True
        )
        return user

    def create_superuser(self, email, full_name=None, password=None):
        user = self.create_user(
                email,
                full_name=full_name,
                password=password,
                is_staff=True,
                is_admin=True,
                is_superuser=True
        )
        return user


class User(AbstractBaseUser):
    statuses    = [('V','Verified'),('U','Unverified')]
    email       = models.EmailField(max_length=255, unique=True)
    full_name   = models.CharField(max_length=255, blank=True, null=True)
    is_active   = models.BooleanField(default=True) # can login 
    staff       = models.BooleanField(default=False) # staff user non superuser
    Agent       = models.BooleanField(default=False) 
    admin       = models.BooleanField(default=False) # superuser 
    timestamp   = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField(upload_to="profile",blank=True)
    status      = models.CharField(max_length=1,choices=statuses)

    USERNAME_FIELD = 'email' #username
    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = [] #['full_name'] #python manage.py createsuperuser

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        if self.is_admin:
            return True
        return self.staff

    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_admin(self):
        return self.Agent


=======

# Create your models here.
>>>>>>> de971c457c57b32399128ec0900d27bd168bb331
