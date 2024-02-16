from django.urls import path
from . import views
from booking_app.views import ModifyView
app_name = 'booking'

urlpatterns = [
    path('', views.index, name='home'),
    path('room/<int:id>/', views.room, name='room'),
    path('room/modify/<int:id>', ModifyView.as_view(), name='modify'),

]