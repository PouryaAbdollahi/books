from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):  # create creation form for custom user
    class Meta:
        model = get_user_model()  # get custom user form AUTH_USER_MODEL
        fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):  # create change form for custom user
    class Meta:
        model = get_user_model()  # get custom user form AUTH_USER_MODEL
        fields = ('email', 'username',)
