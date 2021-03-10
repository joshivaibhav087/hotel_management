from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Account
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from booking.models import Booking

# Create your views here.
def register_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            phone = request.POST['phone']
            age = request.POST['age']
            gender = request.POST['gender']
            id_prof = request.FILES['idproof']
            password = request.POST['password']
            password1 = request.POST['password1']

            user = User.objects.create_user(username = username, first_name = first_name, last_name =last_name, email = email, password = password)
            user.save()
            account = Account(user=user, age = age, phone = phone, id_proof = id_prof, gender = gender)
            account.save()
            return redirect("/account/login/")
    else:
        return redirect('/account/login')   

    return render(request, "account/register.html")

def logins_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if request.user.is_superuser:
                     return redirect('/account/booking-list/')
                return redirect("/booking/booking/")
    else:
        return redirect("/")

    return render(request,'account/login.html')


def logout_view(request):
    logout(request)
    return redirect("/account/login/")


def booking_list_view(request):
    booking = Booking.objects.all()
    return render(request, "account/bookinglist.html", {'booking': booking})