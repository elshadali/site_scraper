from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link
from django.http import HttpResponseRedirect


def scraper(request):

    if request.method == 'POST':
        site = request.POST.get('site', '')
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')

        for link in soup.find_all('a'):
            link_adress = link.get('href')
            link_name = link.string
            Link.objects.create(address=link_adress, name=link_name)
        
        return HttpResponseRedirect('/')

    else:
        data = Link.objects.all()

    return render(request, 'main/link_list.html', {'data': data})


def clear(request):

    Link.objects.all().delete()
    
    return render(request, 'main/link_list.html')


