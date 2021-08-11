from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import password_validation
from .models import UserProfile
class CustomUserCreationForm(UserCreationForm):
	
	email = forms.EmailField(label="Email:", required=True, widget=forms.EmailInput(
		attrs={'autofocus': True}
	))
	username = forms.CharField(
		label="Имя пользователя:", 
		max_length=150
	)
	
	password1 = forms.CharField(
		widget=forms.PasswordInput,
		label="Пароль:",
		required=True,
		strip=True,
		help_text=password_validation.password_validators_help_text_html(),
	)
	password2 = forms.CharField(
		widget=forms.PasswordInput,
		required=True,
		label="Подтверждение пароля:",
		strip=True,
		help_text=password_validation.password_validators_help_text_html(),
	)
	class Meta:
		model = User 
		fields = ['email', 'username' , 'password1', 'password2']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')
		if email and User.objects.filter(email=email).exclude(username=username).count():
			raise forms.ValidationError('Этот почтовый адрес уже используется! Пожалуйста введите другой!')
		return email
		



class CustomUserEditForm(UserChangeForm):
	email = forms.EmailField(
		label="Email:", 
		widget=forms.EmailInput(attrs={'autofocus': True}), 
	)
	username = forms.CharField(
		label="Имя пользователя:", 
		max_length=150,
	)
	
	class Meta: 
		model = UserProfile 
		fields = ['email', 'username']


