from django.shortcuts import render

# Create your views here.
def home(request):
    """
    View function for the blog home page
    """
    return render(request, 'blog/home.html', {
        'title': 'Blog Home'
    })
