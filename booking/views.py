from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
# from booking.forms import UserRegisterForm, ReceptionistRegisterForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login, logout
# from django import forms
# from .models import  Room
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.db import IntegrityError

def RoomList(request):
    return render(request,'home.html')

def about(request):
    return render(request,'hotel/about.html')

#room_types = RoomType.objects.all()
# room = Room.objects.all()
# room_status = RoomStatus.objects.all()
# context = {'rooms': room_types,'room_status':room_status,'room_no':room}
#
# def rooms(request):
#     return render(request, 'hotel/rooms.html', context)
#
# def rooms_detailed_view(request, room_id):
#     room_detail = get_object_or_404(RoomType, pk=room_id)
#     return render(request, 'hotel/rooms_views.html',{'room': room_detail,'rooms': room_types,'room_no':room})
#
# def booking(request,room_id):
#     room_detail = get_object_or_404(RoomType, pk=room_id)
#     return render(request, 'hotel/booking.html',{'room': room_detail,'rooms': room_types,'room_no':room})
#
# # payment
# def payment(request,room_id):
#     room_detail = get_object_or_404(RoomType, pk=room_id)
#     return render(request, 'hotel/payment.html',{'room': room_detail,'rooms': room_types,'room_no':room})
#
# #authorization and authentication
# def admin_create(request):
#     if request.method == "POST":
#        form = UserRegisterForm(request.POST)
#        if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, "Your account has been created successfully! You are now able to log in" + username)
#             return redirect('home')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'home.html', {'form': form})
# #
# # def register_receptionist(request):
# #     if request.method == "POST":
# #        form = ReceptionistRegisterForm(request.POST)
# #        if form.is_valid():
# #           form.save()
# #           first_name = form.cleaned_data.get('first_name')
# #           messages.success(request, "Your account has been created successfully as a Receptionist! You are now able to log in" + first_name)
# #           return redirect('admin-login')
# #     else:
# #         form = ReceptionistRegisterForm()
# #     return render(request, 'hotel/register_Reception.html', {'form': form})
#
# # def admin_create(request):
# #     if request.method == 'GET':
# #         return render(request, 'admin_create.html', {'form': UserCreationForm()})
# #     else:
# #         if request.POST['password1'] == request.POST['password2']:
# #             try:
# #                 user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
# #                 user.save()
# #                 login(request, user)
# #                 return redirect('home')
# #             except IntegrityError:
# #                 return render(request, 'create_admin.html', {'form': UserCreationForm(), 'error': 'Username already exists.'})
# #         else:
# #             return render(request, 'create_admin.html', {'form': UserCreationForm(), 'error': 'Password did not match'})
#
#
# @login_required
# def logoutuser(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect('index')
#
# @login_required
# def profile(request):
#     return render(request, 'hotel/profile.html')
#
# @login_required
# def dashboard(request):
#     return render(request, 'hotel/dashboard.html', {'dash': 'This is the dashboard'})
#
# def admin_list(request):
#     hotel_admin_list = User.objects.all()
#     return render(request, 'hotel/admin_list.html', {'admin_lists': hotel_admin_list})
#
# def show_admin(request, uuid):
#     display_admin = Receptionist.objects.get(uuid(uuid))
#     return render(request, 'hotel/show_admin.html', {'show_admin': display_admin})
#
# def edit_admin(request, id):
#     pass
#
# def delete_admin(request, id):
#     pass
#
# def logs(request):
#     pass
