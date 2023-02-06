from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# <----------------------------------------------- BAND --------------------------------------------->
from bands.models import Band
from bands.forms import BandForm



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
        form = BandForm(request.POST)
        if form.is_valid():
            Band.objects.create(
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
            'form' : BandForm(
                initial = {
                'name_band':band.name_band,
                'members':band.members,
                'musical_genre':band.musical_genre,
                'ig':band.ig,
                'contact':band.contact
                }
            ),
        }
        return render(request, 'bands/update-band.html', context=context)

    elif request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band.name_band=form.cleaned_data['name_band']
            band.members=form.cleaned_data['members']
            band.musical_genre=form.cleaned_data['musical_genre']
            band.ig=form.cleaned_data['ig']
            band.contact=form.cleaned_data['contact']
            band.save()

            context = {
                'message' : 'Banda actualizada🤘🏼!'
            }

        else:
            context = {
                'form_errors' : form.errors,
                'form' : BandForm(
                    initial = {
                    'name_band':band.name_band,
                    'members':band.members,
                    'musical_genre':band.musical_genre,
                    'ig':band.ig,
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
            'form' : TurnForm()
        }
        return render(request, 'turns/create-turn.html', context=context)

    elif request.method == 'POST':
        form = TurnForm(request.POST)
        if form.is_valid():
            Turn.objects.create(
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
                'form' : TurnForm(),
            }
    return render(request, 'turns/create-turn.html', context=context)

class TurnListView(ListView):
    model = Turn
    template_name = 'turns/turns-list.html'

class TurnDeleteView(DeleteView):
    model = Turn
    template_name = 'turns/cancel-turn.html'
    success_url = '/turns/turns-list/'