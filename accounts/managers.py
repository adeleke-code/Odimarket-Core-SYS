from django.contrib.auth.base_user import BaseUserManager







class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

    def create_admin(self, email, password=None, **extra_fields):
        admin = self._create_user(email, password, is_admin=True, is_staff=True, **extra_fields)

        admin.save(using=self._db)

        return admin
    def create_artisan(self, email, password, **extra_fields):
        artisan = self._create_user(email, password, is_user=True, is_artisan=True, **extra_fields)

        artisan.save(using=self._db)

    def create_user(self, email, password=None, **extra_fields):
        user = self._create_user(email, password, is_user=True, **extra_fields)


        user.save(using=self._db)
        
        return user