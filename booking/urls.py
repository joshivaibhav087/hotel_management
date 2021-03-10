from django.urls import path
from . import views
app_name = "booking"
urlpatterns = [
    # path("register/", views.register_view, name = "register"),
    path("booking/", views.booking, name='booking'),
    # path("booking-details/", views.booking_details, name='booking_details'),

]