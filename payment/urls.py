from django.urls import path
from . import views
app_name = "payment"
urlpatterns = [
    # path("register/", views.register_view, name = "register"),
    path("payment/", views.payment,name="payment"),
    path("booking_confirm/", views.booking_confirm, name="confirm"),
]