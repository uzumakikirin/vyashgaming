
from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_view, name='event'),
    path('details/<int:event_id>', views.event_detail_view, name='eventdetail'),
    path('register/', views.event_register_view, name='register'),
]