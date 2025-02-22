from django.shortcuts import render, redirect
from .helpers.url_helper import validate_url
from .models import UrlShort
import uuid
import hashlib
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    objects_list = UrlShort.objects.all()
    p = Paginator(objects_list, 6)
    page = request.GET.get("page")
    shorts_page = p.get_page(page)

    shorts = []
    base_url = request.build_absolute_uri('/')
    
    for object in shorts_page:
        url_hash_redirect = base_url + 'urlshortener/urlredirect/' + object.url_hash
        origin_domain = object.original_url.split('/')[2]
        shorts.append({'url_hash': url_hash_redirect, 'hash': object.url_hash, 'origin': origin_domain})

    return render(request, 'urlshortener/create.html', {
        'shorts': shorts,
        'shorts_page': shorts_page,
    })

def create(request):
    original_url = request.POST.get('original_url', None)

    if not original_url:
        return render(request, 'urlshortener/create.html', {
            'error_msg': 'url required'
        })
    
    if not validate_url(original_url):
        return render(request, 'urlshortener/create.html', {
            'error_msg': 'not valid url'
        })
    
    q = UrlShort.objects.filter(original_url=original_url)

    if len(q):
        url_object = q.first()
        result_url_hash = url_object.url_hash
        base_url = request.build_absolute_uri('/')
        url_hash_redirect = base_url + 'urlshortener/urlredirect/' + url_object.url_hash
        return render(request, 'urlshortener/short_result.html', {
            'hash': result_url_hash,
            'url_hash_redirect': url_hash_redirect
        })
    else:
        unique_id = uuid.uuid4().hex
        hash_object = hashlib.sha256(unique_id.encode())
        new_hash = hash_object.hexdigest()
        new_url_short = UrlShort.objects.create(url_hash=new_hash, original_url=original_url)
        new_url_short.save()

        base_url = request.build_absolute_uri('/')
        url_hash_redirect = base_url + new_url_short.url_hash
        return render(request, 'urlshortener/short_result.html', {
            'hash': new_url_short.url_hash,
            'url_hash_redirect': url_hash_redirect
        })

def hash_redirect(request, hash):
    objects = UrlShort.objects.filter(url_hash=hash)
    url = objects.first()
    if url:
        return redirect(url.original_url)
    else:
        return render(request, 'urlshortener/create.html', {
            'error_msg': 'not rediect found'
        })