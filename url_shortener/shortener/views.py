from django.shortcuts import render, get_object_or_404, redirect
from .forms import URLForm
from .models import URL
import random
import string

# Create your views here.

def generate_short_url():
    return ''.join(random.choice(string.ascii_letters + string.digits))

def home(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            short_url = generate_short_url()
            url, created = URL.objects.get_or_create(original_url=original_url, defaults={'short_url': short_url})
            return render(request, 'shortener/home.html', {'form': form, 'short_url': url.short_url}) 
    else:
        form = URLForm()
    return render (request, 'shortener/home.html', {'form': form})

def redirect_url(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    return redirect(url.original_url)