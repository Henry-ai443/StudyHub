from django.forms import ModelForm, forms
from .models import Room, User
from django.contrib.auth.forms import UserCreationForm
from Base.models import User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        exclude = ['host', 'participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'bio']



from django import forms
from django.contrib.auth.forms import UserCreationForm
from Base.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)  # only email field since password fields come from UserCreationForm

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove username field (not needed, since email is USERNAME_FIELD)
        self.fields.pop('username', None)

        # Add placeholders or customize widgets (optional)
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email

