from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'urlshortener/create.html')

def create(request):
    pass