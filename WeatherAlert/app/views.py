"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from app.forms import SignUpForm, ProfileForm#, VerifyForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from app.models import UsersProfile
from django.contrib.auth.models import User
from app import YahooWeather
from app import GoogleLocator
from app import Twilio


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )


def weather(request):

    """Renders the weather page."""
    assert isinstance(request, HttpRequest)

    #magic number
    TEMPERATURE = 1
    CONDITIONS = 2
    HIGH = 3
    LOW = 4
    IMAGE= 5
    LOCTION = 6

    data = UsersProfile.objects.get(username__username=request.user.username)

    #Get Objects for weather and loction
    weather = YahooWeather.Weather()
    location = GoogleLocator.GeoCodingClient()

    #get Lat and Lon for specfic lociton
    data = location.lookup_location(str(data.location))

    #get weather based off lat and lon
    jsonobject = weather.get_forecast(location.Current_Location(data,1),location.Current_Location(data,2))

    weather = {
            'city' : weather.Current_Weather(jsonobject,LOCTION),
            'temperature' : weather.Current_Weather(jsonobject,TEMPERATURE),
            'description' : weather.Current_Weather(jsonobject,CONDITIONS),
            'icon' : weather.get_GIF(weather.Current_Weather(jsonobject,IMAGE))
        }

    context = {'weather' : weather}
    
    return render(request,
                  'app/weather.html',
                  context)



def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():

            user = form.save()
            user.refresh_from_db() 
            user.usersprofile.location = form.cleaned_data.get('location')
            user.usersprofile.phoneNumber = form.cleaned_data.get('phoneNumber')
            user.usersprofile.time = form.cleaned_data.get('time')
            user.usersprofile.acknowledgment = form.cleaned_data.get('acknowledgment')
            
            sendData = Twilio.TwilioClient()
            code = sendData.send_confirmation_code(user.usersprofile.phoneNumber)
            user.usersprofile.generatedVerificationCode = str(code)
            user.usersprofile.save()
            user.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)

            login(request, user)

            return redirect('verify')
    else:
        form = SignUpForm()
    return render(request, 'app/signup.html', {'form': form})


def verify(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            data = UsersProfile.objects.get(username__username=request.user.username)
            data.userVerificationCode = request.POST.get('verify')
            data.save()

            if data.userVerificationCode == data.generatedVerificationCode:
                return redirect('home')

            info = {
                'Error' : 'There is an error with the code you have entered, please try again...',
                }

            context = {'info' : info}
            
            return render(request, 'app/verify.html',context )
    return render(request, 'app/verify.html',{})



def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'app/login.html', {})


def profile(request):

    """Renders the profile page."""
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':

        data = UsersProfile.objects.get(username__username=request.user.username)

        data.location = request.POST.get('location')
        data.time = request.POST.get('time')
        data.save()

        return redirect('profile')
    else:
        if request.user.is_authenticated:
            data = UsersProfile.objects.get(username__username=request.user.username)
          ##  profile = ProfileForm(instance=data)
            profile = {
                'location': data.location,
                'time':data.time,
                }
        return render(request, 'app/profile.html', {'profile':profile})
    return render(request, 'app/profile.html', {})



def cancel(request):

    try:
        request.user.delete()
        logout(request)
        goodbye = {'message':'Your account has been deleted. Thank you for using our service!'}
    except:
        goodbye = {'message':'There was an error deleting your account. Please go back to your profile and try again'}

    
    return render(request, 'app/cancel.html', {'goodbye':goodbye})



