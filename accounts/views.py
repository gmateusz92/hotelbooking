# from django.shortcuts import render, redirect
# from .forms import RegistrationForm
# from .models import Account
# from django.contrib import messages, auth
#
# def register_user(request):
#     if request.method == "POST":
#         form = RegistrationForm(request.POST)
#         if form.is_valid(): #jezeli dane sa prawidlowe
#             first_name = form.cleaned_data['first_name'] #cleaned_data pobiera dane z formularza
#             last_name = form.cleaned_data['last_name']
#             phone_number = form.cleaned_data['phone_number'] #w modelu nie ma phone_number dlatego nie djamye tego w user = account.
#             email = form.cleaned_data['email']
#             username = email.split("@")[0] #nie tworzymy username
#             password = form.cleaned_data['password']
#             #confirm_password = form.cleaned_data['confirm_password']
#             user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password,) #create_user bierze sie z models
#             user.phone_number = phone_number
#             user.save()
#             # if password != confirm_password:
#             #     return redirect('home')
#             messages.success(request, 'Registration succesfull.')
#             return redirect('register')
#     else:
#         form = RegistrationForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'accounts/register.html', context)
#
# def register_user(request):
#     if request.method == "POST":
#         form = RegistrationForm(request.POST)
#         if form.is_valid(): #jezeli dane sa prawidlowe
#             first_name = form.cleaned_data['first_name'] #cleaned_data pobiera dane z formularza
#             last_name = form.cleaned_data['last_name']
#             phone_number = form.cleaned_data['phone_number'] #w modelu nie ma phone_number dlatego nie djamye tego w user = account.
#             email = form.cleaned_data['email']
#             username = email.split("@")[0] #nie tworzymy username
#             password = form.cleaned_data['password']
#             #confirm_password = form.cleaned_data['confirm_password']
#             user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password,) #create_user bierze sie z models
#             user.phone_number = phone_number
#             user.save()
#             # if password != confirm_password:
#             #     return redirect('home')
#             messages.success(request, 'Registration succesfull.')
#             return redirect('register')
#     else:
#         form = RegistrationForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'accounts/register.html', context)
#
#
#
# def login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#
#         user = auth.authenticate(email=email, password=password)
#         if user is not None:
#             auth.login(request, user)
#             #messages.succes(request, 'You are now logiged in.')
#             return redirect('home')
#         else:
#             messages.error(request, 'Invalid login credenctials')
#             return redirect('login')
#     return render(request, 'accounts/login.html')