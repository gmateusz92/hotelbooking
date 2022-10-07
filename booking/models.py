from django.db import models
from django.db.models.deletion import CASCADE
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    otp_code = models.CharField(max_length=6, unique=True, null=True)
    email_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return self.username

class Receptionist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    gender = models.CharField(max_length=6)
    avatar_url = models.CharField(max_length=260, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'Receptionist {self.first_name} {self.last_name}'

class RoomType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=30, unique=True)
    price = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'Room {self.type} price: {self.price}'

class RoomStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'Room {self.status}'

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_type_id = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_status_id = models.ForeignKey(RoomStatus, on_delete=models.CASCADE)
    room_no = models.CharField(max_length=5, unique=True)
    price = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'Room {self.room_no} price:{self.price} is currently {self.room_status_id}'

class PaymentType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'Payment option {self.name}'

class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment_type_id = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(User, on_delete=CASCADE)
    staff_id = models.ForeignKey(Receptionist, on_delete=CASCADE)
    amount = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'Customer {self.customer_id} amount:{self.amount} processed by staff {self.staff_id}'

class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(User, on_delete=CASCADE)
    staff_id = models.ForeignKey(Receptionist, on_delete=CASCADE)
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'Booking by customer {self.customer_id} paid {self.payment_id} for room {self.room_id}'