from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm

from .forms import SignUpForm

from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token

from django.contrib.auth import login
from django.contrib.auth.models import User

from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from re import template

from django.conf import settings
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives

from django.http import HttpResponse

#def signup(request):
#    if request.method == 'POST':
#        form = UserCreationForm(request.POST)
#        if form.is_valid():
#            form.save()
#            username = form.cleaned_data.get('username')
#            raw_password = form.cleaned_data.get('password1')
#            user = authenticate(username=username, password=raw_password)
#            login(request, user)
#            return redirect('home')
#    else:
#        form = UserCreationForm()
        
#    template = "registration/sign_up.html"
#    return render(request, template , {'form': form})

#def signup(request):
#    if request.method == 'POST':
#        form = SignUpForm(request.POST)
#        if form.is_valid():
#            user = form.save()
#            user.refresh_from_db()  # load the profile instance created by the signal
#            user.profile.birth_date = form.cleaned_data.get('birth_date')
#            user.save()
#            raw_password = form.cleaned_data.get('password1')
#            user = authenticate(username=user.username, password=raw_password)
#            login(request, user)
#            return redirect('home')
#    else:
#        form = SignUpForm()
#    template = "registration/sign_up.html"
#    return render(request, template , {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
#        if form.is_valid():
#            user = form.save(commit=False)
#            user.is_active = False
#            user.save()
#            current_site = get_current_site(request)
#            subject = 'Activate Your MySite Account'
#            message = render_to_string('registration/account_activation_email.html', {
#                'user': user,
#                'domain': current_site.domain,
#                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                'token': account_activation_token.make_token(user),
#            })
#            user.email_user(subject, message)
#            return redirect('accounts:account_activation_sent')
        
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            from_email = settings.EMAIL_HOST_USER
            message = render_to_string('registration/account_activation_email.html', {
                'user':user, 
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your blog account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMultiAlternatives(mail_subject, message, from_email=from_email, to=[to_email])
            email.send()
            
        
            return HttpResponse('Please confirm your email address to complete the registration')

    else:
        form = SignUpForm()
    template = "registration/sign_up.html"
    return render(request, template , {'form': form})

def account_activation_sent(request):
    template = 'registration/account_activation_sent.html'
    return render(request, template)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        template = "registration/account_activation_invalid.html"
        return render(request, template)
    









