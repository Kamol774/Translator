from django.shortcuts import render
from django.http import HttpResponse
from .models import Lugat

def index(request):
    soz = request.GET.get('b', '')
    soz = soz.lower()

    if soz and soz!='':
        natija = Lugat.objects.filter(inglizcha=soz).all()
        natija1 = Lugat.objects.filter(uzbekcha=soz).all()
    else:
        natija = None
        natija1 = None

    ctx = {
        'natija': natija or natija1,
        'b': soz,
    }
    return render(request, 'index.html', ctx)

def salom2(request):
    return HttpResponse('Mening sahifam')

# Create your views here.
