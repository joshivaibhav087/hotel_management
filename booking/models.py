from django.db import models
from django.contrib.auth.models import User

# ROOM_CHOICE1 = (
# ("singlebed", "singlebed"),
# ("doublebed", "doublebed"),
# )
# ROOM_CHOICE2 = (
# ("A/C", "A/C"),
# ("non_A/c", "non_A/C"),
# )

# FOOD_CHOICE = (
#     ("want", "want"),
#     ("dontwant","dontwant"),
# )

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    bed_type = models.CharField(max_length=20)
    room_type = models.CharField(max_length=20)
    guest = models.IntegerField()
    food = models.CharField(max_length=20)
    amount = models.IntegerField()
    # patment_mode = models.CharField(max_length=20)
    # acc_no = models.IntegerField()
    # IFSC= models.CharField(max_length=30)
    # cvv = models.IntegerField()

    # status = models.BooleanField()

    def __str__(self):
        return str(self.user) 



