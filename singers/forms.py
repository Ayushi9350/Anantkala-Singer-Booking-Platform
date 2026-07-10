from django import forms
from django.contrib.auth.models import User
from .models import Singer


class SingerRegistrationForm(forms.ModelForm):

    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    contact_phone = forms.RegexField(
        regex=r'^[0-9]{10}$',
        error_messages={
            'invalid': 'Only 10 digit mobile number allowed.'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter 10 digit mobile number',
            'maxlength': '10',
            'oninput': 'this.value=this.value.replace(/[^0-9]/g,"")'
        })
    )

    class Meta:
        model = Singer

        fields = [
            'name',
            'photo',
            'bio',
            'genre',
            'experience_years',
            'price_per_event',
            'contact_email',
            'contact_phone',
            'instagram',
            'youtube'
        ]

    def save(self, commit=True):

        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['contact_email'],
            password=self.cleaned_data['password']
        )

        singer = super().save(commit=False)

        singer.user = user
        singer.is_approved = False

        if commit:
            singer.save()

        return singer
# AANI NICHE ADD KAR
class SingerProfileEditForm(forms.ModelForm):

    contact_phone = forms.RegexField(
        regex=r'^[0-9]{10}$',
        error_messages={
            'invalid': 'Only 10 digit mobile number allowed.'
        }
    )

    class Meta:
        model = Singer

        fields = [
            'name',
            'photo',
            'bio',
            'genre',
            'experience_years',
            'price_per_event',
            'contact_email',
            'contact_phone',
            'instagram',
            'youtube',
        ]