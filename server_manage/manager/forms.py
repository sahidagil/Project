from django import forms
from .models import LoginForm, hostings, domain_model, users_details, purchased_details

class LoginModelForm(forms.ModelForm):
	class Meta:
		model = LoginForm
		fields = ["user_name", "user_pass"]

class hosting_main_form(forms.ModelForm):
	class Meta:
		model = hostings
		fields = "__all__"

class domainForm(forms.ModelForm):
	class Meta:
		model = domain_model
		fields = "__all__"

class usersForm(forms.ModelForm):
	class Meta:
		model = users_details
		fields = "__all__"

class purchaseForm(forms.ModelForm):
	class Meta:
		model = purchased_details
		fields = "__all__"