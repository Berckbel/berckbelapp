from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'urlshortener/create.html')

def create(request):
    original_url = request.POST.get('original_url', None)

    if not original_url:
        return render(request, 'urlshortener/create.html', {
            'error_msg': 'url required'
        })

    return render(request, 'urlshortener/create.html')