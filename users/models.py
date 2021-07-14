from django.db import models

# Create your models here.
class User(models.Model):
      id = models.AutoField(primary_key=True)
      first_name = models.CharField(max_length=100)
      username = models.CharField(max_length=100)
      last_name = models.CharField(max_length=100)
      email = models.CharField(max_length=100, unique=True)
      password = models.CharField(max_length=100)
      confirm_password = models.CharField(max_length=100)
      created_at = models.DateField(auto_now_add=True)
      updated_at = models.DateField(auto_now_add=True)

      def _str_(self):
            return self.first_name