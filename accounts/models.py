from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models.signals import pre_save
from django.utils.translation import gettext_lazy as _

# Create your models here.
from estore_core.utils import slug_pre_save_receiver


# <editor-fold desc="USER MANAGER FOR ACTIVE USER AND STAFF USER AND SUPERUSER">
class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, phone, password=None, dob=None):
        """
        Create and save a User with the given email and password.
        """

        if not email:
            raise ValueError('Users must have an email address')

        # if phone == None:
        #     raise ValueError(_('The phone must be set'))

        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
            dob=dob
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

        # user = self.model(phone=phone, dob=dob)
        #
        # user.is_active = True
        # email = self.normalize_email(email)
        # user.email = email
        # user.set_password(password)
        # user.save()
        # return user

    def create_staff(self, email, phone, password=None, dob=None):
        """
        Create and save a User with the given email and password.
        """
        user = self.create_user(email=email, phone=phone, password=password, dob=dob)

        user.is_staff = True
        user.save(using=self._db)

        return user

    def create_superuser(self, email, phone, password=None, dob=None):
        """
        Create and save a User with the given email and password.
        """
        user = self.create_user(email=email, phone=phone, password=password, dob=dob)

        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


# </editor-fold>


# <editor-fold desc="USER CREATE">
class User(AbstractBaseUser, PermissionsMixin):
    phone = models.BigIntegerField(_('phone number'), unique=True)
    email = models.EmailField(_('Email address'), unique=True)
    dob = models.DateField(_('date of birth'), null=True,
                           blank=True)  # null is database related,blank is validation related use

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # is_superuser= models.BooleanField( default=False)

    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']
    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)

    # this methods must be Required for AbstractBaseUser Model  .
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


pre_save.connect(slug_pre_save_receiver, sender=User)
# </editor-fold>
