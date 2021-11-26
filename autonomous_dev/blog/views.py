from django.shortcuts import render
from .models import Post


def home(request):
    """This view is the home page. The blog will be shown here."""
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

