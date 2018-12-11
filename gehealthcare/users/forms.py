import logging
from django import forms
from django.contrib.auth import authenticate
from .models import User

logger = logging.getLogger()

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    error_messages = {
        'invalid_login': ("Please enter a correct %(email)s and password. "
                          "Note that both fields may be case-sensitive."),
        'inactive': ("This account is inactive."),
        'does_not_exist': ("User does not exist"),
    }

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        logger.debug(email)
        password = cleaned_data.get('password')
        try:
            user = User.objects.get(email=email)
            username = user.get_username()
        except User.DoesNotExist:
            raise forms.ValidationError(
                self.error_messages['does_not_exist'],
                code='does_not_exist',
                params={'username: "email" '},
            )
        if username and password:
            self.user_cache = authenticate(username=email,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': 'email'},
                )
            else:
                self.confirm_login_allowed(self.user_cache)
        return cleaned_data

    def confirm_login_allowed(self, user):
        """
        controls whether the given user may log in. This is the policy setting
        independent of end-user authentication. This default behaviour is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``forms.ValidationError``.

        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )
