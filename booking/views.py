from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from singers.models import Singer
from singers.forms import SingerRegistrationForm
from .models import Booking
from .forms import BookingForm
from singers.forms import SingerProfileEditForm


@login_required
def book_singer(request, singer_id):

    singer = get_object_or_404(
        Singer,
        pk=singer_id,
        is_available=True
    )

    if request.method == 'POST':

        form = BookingForm(request.POST)

        if form.is_valid():

            booking = form.save(commit=False)

            booking.user = request.user
            booking.singer = singer
            booking.total_amount = singer.price_per_event

            booking.save()

            messages.success(
                request,
                f'Booking request for {singer.name} submitted successfully!'
            )

            return redirect('my_bookings')

    else:

        form = BookingForm()

    return render(
        request,
        'booking/book_singer.html',
        {
            'form': form,
            'singer': singer
        }
    )


@login_required
def my_bookings(request):

    bookings = Booking.objects.filter(
        user=request.user
    )

    return render(
        request,
        'booking/my_bookings.html',
        {
            'bookings': bookings
        }
    )


from django.contrib.auth import authenticate, login, logout


# Singer Register
def singer_register(request):

    if request.method == 'POST':

        form = SingerRegistrationForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Registration request sent to admin.'
            )

            return redirect('singer_login')

    else:

        form = SingerRegistrationForm()

    return render(
        request,
        'booking/singer_register.html',
        {
            'form': form
        }
    )


# Singer Login
def singer_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            try:

                singer = Singer.objects.get(user=user)

                if not singer.is_approved:

                    messages.error(
                        request,
                        'Admin approval pending.'
                    )

                    return redirect('singer_login')

                login(request, user)

                return redirect('singer_dashboard')

            except Singer.DoesNotExist:

                messages.error(
                    request,
                    'You are not registered as a singer.'
                )

        else:

            messages.error(
                request,
                'Invalid username or password.'
            )

    return render(
        request,
        'booking/singer_login.html'
    )


# Singer Logout
def singer_logout(request):

    logout(request)

    return redirect('singer_login')


# Singer Dashboard
@login_required
def singer_dashboard(request):

    try:

        singer = Singer.objects.get(
            user=request.user
        )

    except Singer.DoesNotExist:

        messages.error(
            request,
            'Singer profile not found.'
        )

        return redirect('singer_login')

    bookings = Booking.objects.filter(
        singer=singer
    ).order_by('-created_at')

    return render(
        request,
        'booking/singer_dashboard.html',
        {
            'singer': singer,
            'bookings': bookings
        }
    )


# Accept / Reject
@login_required
def update_booking_status(request, booking_id):

    try:

        singer = Singer.objects.get(
            user=request.user
        )

    except Singer.DoesNotExist:

        return redirect('singer_login')

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        singer=singer
    )

    if request.method == 'POST':

        action = request.POST.get('action')

        if action == 'accept':

            booking.status = 'confirmed'

        elif action == 'reject':

            booking.status = 'cancelled'

        booking.save()

        messages.success(
            request,
            'Booking updated!'
        )


    return redirect('singer_dashboard')

@login_required
def edit_singer_profile(request):

    singer = get_object_or_404(
        Singer,
        user=request.user
    )

    if request.method == 'POST':

        form = SingerProfileEditForm(
            request.POST,
            request.FILES,
            instance=singer
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Profile updated successfully!'
            )

            return redirect('singer_dashboard')

    else:

        form = SingerProfileEditForm(
            instance=singer
        )

    return render(
        request,
        'booking/edit_profile.html',
        {
            'form': form
        }
    )

@login_required
def cancel_booking(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user
    )

    booking.status = 'cancelled'
    booking.save()

    messages.success(
        request,
        'Booking cancelled successfully.'
    )

    return redirect('my_bookings')