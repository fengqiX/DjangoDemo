import hashlib
import re
import django.forms as forms
from django.core.exceptions import ValidationError
from ..models import User

USERNAME_PATTERN = re.compile(r'\w{4,20}')


class RegisterForm(forms.ModelForm):
    repassword = forms.CharField(min_length=8, max_length=20)

    def clean_username(self):
        username = self.cleaned_date['username']
        if not USERNAME_PATTERN.fullmatch(username):
            raise ValidationError("username is invalid!")
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8 or len(password) > 20:
            raise ValidationError("Password is invalid!")
        return to_md5_hex(self.cleaned_data['password'])

    def clean_repassword(self):
        repassword = to_md5_hex(self.cleaned_data['repassword'])
        if repassword != self.cleaned_data['password']:
            raise ValidationError('Two passwords are not same')
        return repassword
    class Meta:
        model=User
        exclude = ('no','reg_date')

def to_md5_hex(message):
    return hashlib.md5(message.encode()).hexdigest()