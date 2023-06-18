from django.db import models

class SignUpUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name