from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
("male", "male"),
("female", "female"),
("others","others"),
)
# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField()
    age = models.IntegerField()
    id_proof = models.ImageField(upload_to="idprof")
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)

    def __str__(self):
        return str(self.user)

