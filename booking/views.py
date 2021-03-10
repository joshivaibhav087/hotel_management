from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Booking
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.
def booking(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            checkin_date = request.POST['checkin']
            checkout_date = request.POST['checkout']
            bed_type = request.POST['cmbitems1']
            room_type = request.POST['cmbitems2']
            guest = request.POST['guest']
            food = request.POST['cmbitems3']
            amount = request.POST['amount1']
            # status = request.POST['status']

            booking = Booking(user = request.user, checkin_date = checkin_date,checkout_date = checkout_date, bed_type=bed_type, room_type = room_type, guest = guest, food = food, amount = amount)
            booking.save()
            # payment = Payment.objects.get(user=request.user)
            # id = payment.id
            return redirect("/payment/payment/")
    return render(request,"booking/booking_page.html")

# def booking_details(request):
#     booking = Booking.objects.all()
#     return render(request, 'booking/payment.html',{'booking':booking})

def redirect_view(request):
    return redirect("/booking/booking/")




    
