from django import forms


class Signupform(forms.Form):
    fName = forms.CharField(label='', max_length=100,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'First Name',
                                    'id': 'fName'
                                }
                            )
                            )
    lName = forms.CharField(label='', max_length=100,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Last Name',
                                    'id': 'lName'
                                }
                            )
                            )
    uName = forms.CharField(label='', max_length=20, min_length=3,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'User Name',
                                    'id': 'uName'
                                }
                            )
                            )
    password = forms.CharField(label='', max_length=20, min_length=5,
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Password',
                                       'id': 'password'
                                   }
                               )
                               )
    cpassword = forms.CharField(label='', max_length=20, min_length=5,
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Confirm Password',
                                        'id': 'cpassword'
                                    }
                                )
                                )


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
