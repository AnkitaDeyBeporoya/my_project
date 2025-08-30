from django import forms
from django.core.validators import validate_email, RegexValidator
from django.core.exceptions import ValidationError
from.models import userdata

class userinfoform(forms.ModelForm):

    def email(self):
        email = self.cleaned_data.get('email')
        
        try:
            validate_email(email)
            # spart = email.split('@')[-1].split('.')[0].lower()
            if email.endswith(('.com'or'.org'or'.net')):
                print("mail is  valid!")
            return email
            
        except ValidationError:
            raise ValidationError("Please enter a valid email address")
        
    def phone_no(self):
        phone = self.cleaned_data.get('phone_no')
        if not phone.isdigit() or len(phone) < 10:
            raise ValidationError("Enter a valid 10-digit phone number")
        return phone


    class Meta:
        model=userdata
        fields=['name', 'age', 'email', 'phone_no', 'password', 'status']
        widgets={
            'password': forms.PasswordInput(),
            'email': forms.EmailInput(attrs={
                'placeholder': 'example@domain.com',
                'class': 'email-input'}),
            'status': forms.Select(choices=[
                (0, 'active'),
                (1, 'inactive'),
                (5, 'banned')
            ])

        }