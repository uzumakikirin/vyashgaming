from django.shortcuts import render, redirect, get_object_or_404
from event.models import EventDetail

def home_view(request):
    title="Welcome Homepage..."
    events = EventDetail.objects.order_by('-created_at')[:3]
    context = {
        'title':title,
        'events':events,
    }
    return render(request, 'home.html', context)

