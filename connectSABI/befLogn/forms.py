from django import forms


class OTPform(forms.Form):
    OTP = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'aria-describedby': 'emailHelp',
                'placeholder': 'OTP'
            }
        )
    )
