from django.urls import path
from . import views
from booking_app.views import ModifyView, NewRoomView, DeleteView, ReservationView, SearchView

app_name = 'booking'

urlpatterns = [
    path('', views.index, name='home'),
    path('room/<int:id>/', views.room, name='room'),
    path('room/new', NewRoomView.as_view(), name='new-room'),
    path('room/modify/<int:id>', ModifyView.as_view(), name='modify'),
    path('room/delete/<int:id>', DeleteView.as_view(), name='delete'),
    path('room/reservation/<int:id>', ReservationView.as_view(), name='reservation'),
    path('search/', SearchView.as_view(), name='search'),

]
