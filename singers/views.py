from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Singer, Genre, ContactMessage, SingerLike, GalleryVideo


def home(request):
    featured_singers = Singer.objects.filter(
        featured=True,
        is_approved=True,
        is_available=True
    )[:6]

    all_genres = Genre.objects.all()
    total_singers = Singer.objects.count()

    context = {
        'featured_singers': featured_singers,
        'genres': all_genres,
        'total_singers': total_singers,
    }

    return render(request, 'singers/home.html', context)


def singer_list(request):
    singers = Singer.objects.filter(
        is_available=True,
        is_approved=True
    )

    genres = Genre.objects.all()
    genre_filter = request.GET.get('genre')

    if genre_filter:
        singers = singers.filter(genre__id=genre_filter)

    context = {
    'singers': singers,
    'genres': genres,
    'selected_genre': genre_filter,
    'liked_singers': SingerLike.objects.filter(user=request.user).values_list('singer_id', flat=True) if request.user.is_authenticated else [],
}
    return render(request, 'singers/singer_list.html', context)


def singer_detail(request, pk):
    singer = get_object_or_404(Singer, pk=pk)
    gallery = singer.gallery.all()

    is_liked = False

    if request.user.is_authenticated:
        is_liked = SingerLike.objects.filter(
            singer=singer,
            user=request.user
        ).exists()

    context = {
        'singer': singer,
        'gallery': gallery,
        'is_liked': is_liked,
        'likes_count': singer.likes.count(),
    }

    return render(request, 'singers/singer_detail.html', context)


@login_required
def toggle_like(request, pk):
    singer = get_object_or_404(Singer, pk=pk)

    like, created = SingerLike.objects.get_or_create(
        singer=singer,
        user=request.user
    )

    if not created:
        like.delete()

    return redirect('singer_detail', pk=pk)


def about(request):
    return render(request, 'singers/about.html')


def contact(request):
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )

    return render(request, 'singers/contact.html')

def gallery(request):
    videos = GalleryVideo.objects.all()
    return render(
        request,
        'singers/gallery.html',
        {'videos': videos}
    )