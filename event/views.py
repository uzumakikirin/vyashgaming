from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mass_mail, BadHeaderError
from django.conf import settings
from event.models import *
from event.forms import EventForm
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def event_view(request):
    title="Welcome Eventpage."
    events = EventDetail.objects.all()[:6]
    context = {
        'title':title,
        'events':events,
    }
    return render (request,'event/event.html', context)

def event_detail_view(request, event_id):
    title="Event Detail Page"
    eventdetail = get_object_or_404(EventDetail,pk=event_id)
    context = {
        'title':title,
        'eventdetail':eventdetail,
    }
    return render (request,'event/eventdetail.html', context)

def event_register_view(request):
    if request.method == 'POST':
        form = EventForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            fullname = form.cleaned_data.get("fullname")
            squad = form.cleaned_data.get('squadname')
            membernum = form.cleaned_data.get('membernumber')

            message = "You have been register. Check the details" + " Email " + email + " Name " + fullname  + " Sqaud Name " + squad + " members " + membernum

            print(email)
            form.save()
            try:
                message1 = (
                            'Registration Message',
                            'A Team had registered',
                            email,
                            [settings.EMAIL_HOST_USER]
                            )
                message2 = ('Registration Confirmation',
                            message,
                            settings.EMAIL_HOST_USER,
                            [email]
                            )
                send_mass_mail((message1, message2), fail_silently=False)
            except BadHeaderError:
                return messages.error(request, 'Email is not valid.')
            messages.success(request, "Registration Completed")
            return redirect('register')
    else:
        form = EventForm()
    return render(request, 'event/register.html', {'form':form,})
