from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Payment(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    payment_mode = models.CharField(max_length=20)
    card_no = models.IntegerField()
    IFSC= models.CharField(max_length=30)
    cvv = models.IntegerField()
    amount_paid = models.IntegerField(default= 1)
    

    # status = models.BooleanField()

    def __str__(self):
        return str(self.user)
