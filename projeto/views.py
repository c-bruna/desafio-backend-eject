from django.shortcuts import render
from multiprocessing import context

from projeto.models import Inicio
from projeto.models import BoldFeatures
from projeto.models import MeetLaurel
from projeto.models import StayInTheKnow
from projeto.models import Contato
from projeto.models import EnviarEmail

def home(request):
    inicio = Inicio.objects.last()
    boldfeatures = BoldFeatures.objects.last()
    meetlaurel = MeetLaurel.objects.last()
    stayintheknow = StayInTheKnow.objects.last()
    contato = Contato.objects.last()
    enviaremail = EnviarEmail.objects.last()

    context = {
        'inicio' : inicio,
        'boldfeatures' : boldfeatures,
        'meetlaurel' : meetlaurel,
        'stayintheknow' : stayintheknow,
        'contato' : contato,
        'enviaremail' : enviaremail
    }

    if request.method == 'POST':
        email = request.POST['email']

        form = EnviarEmail(email=email)
        form.save()

    return render (request, 'index.html', context)


