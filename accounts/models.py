from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.CharField(max_length=300, unique=True)
    phone = models.CharField(max_length=300)
    password = models.CharField(max_length=450)
    is_active = models.BooleanField(default=True)
    is_artisan = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []



    def __str__(self):
        return self.email

# {
#     "first_name": "John",
#     "last_name": "Doe",
#     "email": "johndoe@gmail.com",
#     "phone": "+234708646664",
#     "password": "password123",
#     "product_id": "10aa2b4a-cf31-489e-8071-4d6f6b8f8806",
#     "client_id": "cc6e3604-4b22-4b3c-9bce-ef55572085fa",
#     "group_id": "cc6e3604-4b22-4b3c-9bce-ef55572085fa",
#     "role_id": "cc6e3604-4b22-4b3c-9bce-ef55572085fa"
# }

# """
# {
# PRODUCT_CODE_MAIN: 'ODI-MKT',
# PRODUCT_CODE_CORE: 'ODI-HMT',
# }

# buyer: {
#   role: 'BUYER',
#   client: 'BUYER'
# },

# artisan: {
#   role: 'ARTISAN',
#   client: 'ARTISAN'
# }

# """