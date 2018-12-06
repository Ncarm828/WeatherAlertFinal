"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from app.models import UsersProfile
from app import Twilio
import re


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class SignUpForm(UserCreationForm):
    location = forms.CharField(max_length=30, required=True, help_text='Zip Code.')
    phoneNumber = forms.CharField(max_length=30, required=True, help_text='Phone Number Format: XXX-XXX-XXXX')
    time = forms.CharField(max_length=10, required=True, help_text='Enter time as HH:MM AM/PM or H:MM AM/PM and minute must be a multiple of 15')
    acknowledgment = forms.BooleanField(help_text = 'By checking this, you agree to recieve text messages every day from twiliow at the time you specified above. Go to the home page for more information')

    class Meta:
        model = User
        fields = ('username', 'location', 'phoneNumber', 'time', 'acknowledgment', 'password1', 'password2')


    #Validate Zip code from user
    def clean_location(self):
        data = self.cleaned_data['location']
        zipCode = re.compile(r"^[0-9]{5}(?:-[0-9]{4})?$")

        if zipCode.match(data):
            return data
        else:
            raise forms.ValidationError("This is not a valid Zip Code")

    #Validate phone number from user
    def clean_phoneNumber(self):
        data = self.cleaned_data['phoneNumber']
        PhoneNumber = re.compile("^[\dA-Z]{3}-[\dA-Z]{3}-[\dA-Z]{4}$")
        
        if PhoneNumber.match(data):
            return data
        else:
            raise forms.ValidationError("This is not a valid Phone Number")
    
    #Validate time from user
    def clean_time(self):
        data = self.cleaned_data['time']
        TIME = re.compile("^ *(1[0-2]|[1-9]):[0-5][0-9] *(a|p|A|P)(m|M) *$")
        if data is None:
            raise forms.ValidationError("You must select a time to recieve weather conditions")
        elif TIME.match(data):

            #format is ##:## ##
            time = data.split(":")
            temp = time[1].split(" ")

            hour = time[0]
            minute = temp[0]

            try:
               assert minute in ["00", "15", "30", "45"]
               return data
            except:
                raise forms.ValidationError("The minutes must be either '00', '15', '30', '45', not %s" % minute)
            return data
        else:
            raise forms.ValidationError("Please enter correct format")
        raise forms.ValidationError("Unkown Error has occured. Please re-enter the correct information")
        

    #Validate acknowledgment agreement from user
    def clean_acknowledgment(self):
        data =  self.cleaned_data['acknowledgment']
        if not data:
            raise forms.ValidationError("You must accept the terms before registering")
        return data



class ProfileForm(UserChangeForm):
    location = forms.CharField(max_length=30, required=True, help_text='Zip Code.')
    phoneNumber = forms.CharField(max_length=30, required=True, help_text='Phone Number Format: XXX-XXX-XXXX')
    time = forms.CharField(max_length=10, required=True, help_text='Enter time as HH:MM AM/PM or H:MM AM/PM')
    acknowledgment = forms.BooleanField()

    class Meta:
        model = User
        fields = ('location', 'phoneNumber', 'time', 'acknowledgment','password')




