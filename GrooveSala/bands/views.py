from django.shortcuts import render

from bands.models import Band
from bands.forms import BandForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView



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
                own_instruments=form.cleaned_data['own_instruments'],
                ig=form.cleaned_data['ig'],
                contact=form.cleaned_data['contact'],
            )

            context = {
                'message' : f'Banda en lista 🤘🏼!'
            }

        else:
            context = {
                'form_errors' : form.errors,
                'form' : BandForm(),
            }
        return render(request, 'bands/create-band.html', context=context)

class BandListView(ListView):
    model = Band
    template_name = 'bands/bands-list.html'

class BandDeleteView(DeleteView):
    model = Band
    template_name = 'bands/delete-band.html'
    success_url = '/bands/bands-list/'