from django.contrib.auth.forms import UserCreationForm
from share.models import User


# class RegisterForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email', 'password1', 'password2')