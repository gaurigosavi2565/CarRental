from django.shortcuts import render, get_object_or_404
from .models import Car, Booking

def car_list(request):
    cars = Car.objects.filter(available=True)
    return render(request, 'client/car_list.html', {'cars': cars})

def book_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        booking_start_date = request.POST.get('booking_start_date')
        booking_end_date = request.POST.get('booking_end_date')
        Booking.objects.create(
            car=car,
            client_name=client_name,
            booking_start_date=booking_start_date,
            booking_end_date=booking_end_date
        )
        car.available = False
        car.save()
        return render(request, 'client/booking_success.html')
    return render(request, 'client/book_car.html', {'car': car})