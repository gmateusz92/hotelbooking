from django.contrib import admin
from .models import User, Receptionist, RoomType, RoomStatus, Room, PaymentType, Payment, Booking

admin.site.register(User)
admin.site.register(Receptionist)
admin.site.register(RoomType)
admin.site.register(RoomStatus)
admin.site.register(Room)
admin.site.register(PaymentType)
admin.site.register(Payment)
admin.site.register(Booking)