from django.shortcuts import render

from django.views.generic import ListView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# <----------------------------------------------- BAND --------------------------------------------->
from bands.models import Band, Event
from bands.forms import BandForm, BandUpdateForm, EventForm



class BandListView(ListView):
    model = Band
    template_name = 'bands/bands-list.html'

def search_band(request):
    if 'search' in request.GET:
        search = request.GET['search']
        bands = Band.objects.filter(name_band__icontains=search)
        
    else:
        bands = Band.objects.all()
    context = {
        'object_list':bands,
    }

    return render(request, 'bands/bands-list.html', context=context)    

@login_required
def create_band(request):
    if request.method == 'GET':
        context = {
            'form' : BandForm(),
        }
        return render(request, 'bands/create-band.html', context=context)

    elif request.method == 'POST':
        form = BandForm(request.POST, request.FILES)
        if form.is_valid():
            Band.objects.create(
                logo=form.cleaned_data['logo'],
                name_band=form.cleaned_data['name_band'],
                members=form.cleaned_data['members'],
                musical_genre=form.cleaned_data['musical_genre'],
                ig=form.cleaned_data['ig'],
                contact=form.cleaned_data['contact'],
            )
            
            context = {
                'message' : f'Banda en lista 🤘🏼!' # Pendiente agregar para que pase el {nombre} de la banda que quedo en lista
            }

        else:
            context = {
                'form_errors' : form.errors,
                'form' : BandForm(),
            }
        return render(request, 'bands/create-band.html', context=context)

@login_required
def update_band(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'GET':
        context = {
            'form' : BandUpdateForm(
                initial = {
                'logo':band.logo,
                'members':band.members,
                'musical_genre':band.musical_genre,
                'own_instruments':band.own_instruments,
                'contact':band.contact
                }
            ),
        }
        return render(request, 'bands/update-band.html', context=context)

    elif request.method == 'POST':
        form = BandUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            band.logo=form.cleaned_data['logo']
            band.members=form.cleaned_data['members']
            band.musical_genre=form.cleaned_data['musical_genre']
            band.contact=form.cleaned_data['contact']
            band.own_instruments=form.cleaned_data['own_instruments']
            band.save()

            context = {
                'message' : 'Banda actualizada🤘🏼!'
            }

        else:
            context = {
                'form_errors' : form.errors,
                'form' : BandUpdateForm(
                    initial = {
                    'logo':band.logo,
                    'members':band.members,
                    'musical_genre':band.musical_genre,
                    'own_instruments':band.own_instruments,
                    'contact':band.contact
                    }
                ),
            }
            return render(request, 'bands/update-band.html', context=context)
    
    return render(request, 'bands/update-band.html', context=context)

class BandDeleteView(LoginRequiredMixin, DeleteView):
    model = Band
    template_name = 'bands/delete-band.html'
    success_url = '/bands/bands-list/'

def create_event(request):
    if request.method == 'GET':
        context = {
            'form' : EventForm(),
        }
        return render(request, 'index.html', context=context)

    elif request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            Event.objects.create(
                date=form.cleaned_data['date'],
                name=form.cleaned_data['name'],
                flyer=form.cleaned_data['flyer'],
            )

            context = {
                'message' : 'Evento cargado!'
            }
            return render(request, 'index.html', context=context)

        else:
            context = {
                'form_errors' : form.errors,
                'form' : EventForm(),
            }
    return render(request, 'index.html', context=context)

class EventListView(ListView):
    model = Event
    template_name = 'index.html'

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'bands/cancel-event.html'
    success_url = '/'
# <----------------------------------------------- TURNS --------------------------------------------->
from bands.models import Turn
from bands.forms import TurnForm, FirstTurnForm


def first_time(request):
    return render(request, 'turns/first-time.html', context={})

def create_first_turn(request):
    if request.method == 'GET':
            context = {
                'form' : FirstTurnForm()
            }
            return render(request, 'turns/create-first-turn.html', context=context)

    elif request.method == 'POST':
        form = FirstTurnForm(request.POST)
        if form.is_valid():
            Turn.objects.create(
                name_band=form.cleaned_data['name_band'],
                members=form.cleaned_data['members'],
                turn_assigned=form.cleaned_data['turn_assigned'],
                own_instruments=form.cleaned_data['own_instruments'],
                contact=form.cleaned_data['contact']
            )

            context = {
                'message' : 'Turno Solicitado! 👍🏼'
            }
            return render(request, 'turns/create-first-turn.html', context=context)

        else:
            context = {
                'form_errors' : form.errors,
                'form' : FirstTurnForm(),
            }
        return render(request, 'turns/create-first-turn.html', context=context)

def create_turn(request):
    if request.method == 'GET':
        context = {
            'form' : TurnForm(initial={
                'name_band':request.user.name_band,
            }
        )
    }
        return render(request, 'turns/create-turn.html', context=context)

    elif request.method == 'POST':
        form = TurnForm(request.POST)
        if form.is_valid():
            Turn.objects.create(
                name_band=form.cleaned_data['name_band'],
                members=form.cleaned_data['members'],
                turn_assigned=form.cleaned_data['turn_assigned'],
                own_instruments=form.cleaned_data['own_instruments']
            )

            context = {
                'message' : 'Turno Solicitado! 👍🏼'
            }
            return render(request, 'turns/create-turn.html', context=context)

        else:
            context = {
                'form_errors' : form.errors,
                'form' : TurnForm(initial={
                    'name_band':request.user.name_band,
                }
            ),
        }
    return render(request, 'turns/create-turn.html', context=context)

def my_turns(request):
    search=request.user.name_band
    turn = Band.objects.filter(name_band__contains=search)
    context = {
        'object_list':turn
    }
    return render(request, 'turns/turns-list.html', context=context)

class TurnListView(ListView):
    model = Turn
    template_name = 'turns/turns-list.html'

class TurnDeleteView(DeleteView):
    model = Turn
    template_name = 'turns/cancel-turn.html'
    success_url = '/turns/turns-list/'