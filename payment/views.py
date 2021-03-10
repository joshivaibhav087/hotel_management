from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Payment
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from booking.models import Booking

# Create your views here.
def payment(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            payment_mode = request.POST['mode']
            card_no = request.POST['card']
            IFSC = request.POST['ifsc']
            cvv = request.POST['cvv']
            name = request.POST['nam']

            booking1 = Booking.objects.filter(user=request.user).last()
            payment = Payment(user = request.user, payment_mode = payment_mode, card_no = card_no, IFSC = IFSC, cvv = cvv, name = name, amount_paid = booking1.amount)
            payment.save()
            return redirect("/payment/booking_confirm/")
        booking1 = Booking.objects.filter(user=request.user).last()

    book = Booking.objects.filter(user=request.user).last()
    return render(request, "booking/payment.html",{'book':book,'booking1':booking1})

def booking_confirm(request):
    confirm = Booking.objects.filter(user=request.user).last()
    return render(request, "booking/confirm.html", {'confirm':confirm})

