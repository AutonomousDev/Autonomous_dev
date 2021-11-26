from django.shortcuts import render

def home(request):
    """This view is the home page. The blog will be shown here."""
    return render(request, 'blog/home.html')

