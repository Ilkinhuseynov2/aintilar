from django.shortcuts import render , HttpResponse
from .models import alinti
import random
# Create your views here.
def random_alinti(request):
    a = alinti.objects.all()
    print(a)
    d = random.choice(a)
    return render(request , 'random.html' , {'cumle' : d.cumle , 'yazar' : d.yazici , 'resim' : d.resim})
def id_alinti(request , id):
    try:
        d = alinti.objects.all()
        d = d[id]
        return render(request , 'random.html' , {'cumle' : d.cumle , 'yazar' : d.yazici , 'resim' : d.resim})
    except:
        return render(request , '404.html')
def yazar_alinti(request , yazar):
    # try:
    d = alinti.objects.all()
    c = []
    for i in d:
        if i.yazici == yazar:
            c.append(i)
        else:
            pass
    return render(request , 'yazar.html' , {'alintilar' : c , 'yazarr' : yazar})
    # except:
        # return render(request , '404.html')
def all_alinti(request):
    return render(request , 'all.html' , {'alintilar' : alinti.objects.all()})
def yazarlar(request):
    c = []
    yazicilar = []
    for i in alinti.objects.all():
        if i.yazici in yazicilar:
            pass
        else:
            yazicilar.append(i.yazici)
            c.append(i)
    print(c)
    return render(request , 'yazarlar.html' , {'yazarlar' : c})