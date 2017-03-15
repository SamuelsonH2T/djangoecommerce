from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import View, TemplateView
from .forms import ContactForm



class IndexView(TemplateView):

    template_name = 'index.html'


index = IndexView.as_view()



#Essa view foi criada na app core pq é generica.

def contact(request):
    success = True
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_mail()
            success = True
    else:
        form = ContactForm()
    context = {
        'form' : form,
        'success': success
    }

    return render(request, 'contact.html', context)
