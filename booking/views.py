from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, "booking/home.html")

    
def booking(request):
    weekdays = validWeekday(20)
    
    validdateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')
        if service == None:
            messages.success(request, "Please Select a service")
            return redirect("booking")
        # Store day and service in django session.
        request.session['day'] = day
        request.session['service'] =service 

        return redirect('bookingSubmit')

    return render(request, 'booking.html', {'weekdays':weekdays, 'validateWeekdays':validateWeekdays})