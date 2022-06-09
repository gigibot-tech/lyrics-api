from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from loginsystem.forms import LoginForm
from loginsystem.forms import UserCreateForm
from loginsystem.forms import ContactForm
from loginsystem.models import Contact
from django.http import HttpResponse
from django.db import IntegrityError



def signin(request):   #login name is not same as inbuild login function

    if request.user.username:
        return redirect(home)

    message = ''
    form = LoginForm()
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user==None:

                message = "Invalid login details"

            else:
                login(request,user)

                # request.session['city'] = 'Bangalore'     #creating session variable
                # request.session['address'] = 'BTM'          #creatinf session variables

                return redirect(home)

    return render(request, 'signin.html', {'form': form, 'message': message})



def signup(request):

    signup_success = ''

    if request.user.username:
        return redirect(home)

    form = UserCreateForm()
    if request.method=='POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():

            user = User()
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password1'])
            user.save()
            signup_success = 'User successfully Registered'
            return redirect(signin)


    return render(request, 'signup.html', {'form': form, 'signup_success': signup_success})


def signout(request):

    logout(request)
    return redirect(signin)


def contact(request):

    message = ""
    form_data = ContactForm()
    if request.method == 'POST':
        form_data = ContactForm(request.POST)
        if form_data.is_valid():

            con = Contact()
            con.name = form_data.cleaned_data['name']
            con.email = form_data.cleaned_data['email']
            con.message = form_data.cleaned_data['message']
            con.save()
            message = "Your message has been successfully submitted"

            # return redirect(index)

    return render(request, 'contact_us.html', {'form_data': form_data, "message_conf":message})


def about(request):

    return render(request, 'about_us.html')

