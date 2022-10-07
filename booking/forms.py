from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import User, Receptionist

# Create your forms here.

class UserRegisterForm(UserCreationForm):
	#
	# username = forms.CharField(max_length=30, )
	# email = forms.EmailField(max_length=254, )
	# phone_number = forms.CharField(max_length=20,)
	# password = forms.CharField(max_length=20)
	# otp_code = forms.CharField(max_length=6, null=True)
	# email_verified = forms.BooleanField(default=False)
	# is_admin = forms.BooleanField(default=False)
	# is_superadmin = forms.BooleanField(default=False)
	# created_at = forms.DateTimeField(auto_now_add=True, null=True)
	# updated_at = forms.DateTimeField(auto_now=True, null=True)

	class Meta:
		model = User
		fields = ['username', 'email']
		#fields = '__all__'


class ReceptionistRegisterForm(ModelForm):
	email = forms.EmailField(required=True)

	class Meta:
		#model = Receptionist
		fields = ["first_name", "last_name", "gender", 'avatar_url',  ]