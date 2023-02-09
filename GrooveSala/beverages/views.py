from django.shortcuts import render
from django.views.generic import ListView

from beverages.models import Beverage
from beverages.forms import BeverageForm


def create_beverage(request):
    if request.method == 'GET':
        context = {
            'form' : BeverageForm(),
        }
        return render(request, 'beverages/create-beverage.html', context=context)

    elif request.method == 'POST':
        form = BeverageForm(request.POST, request.FILES)
        if form.is_valid():
            Beverage.objects.create(
                picture=form.cleaned_data['picture'],
                brand=form.cleaned_data['brand'],
                size=form.cleaned_data['size'],
                quantity=form.cleaned_data['quantity'],
            )

            context = {
                'message' : 'La nueva bebida ha sido cargada!'
            }
            return render(request, 'beverages/create-beverage.html', context=context)

        else:
            context = {
                'form_errors' : form.errors,
                'form' : BeverageForm(),
            }
    return render(request, 'beverages/create-beverage.html', context=context)

def search_beverages(request):
    if 'search' in request.GET:
        search = request.GET['search']
        beverages = Beverage.objects.filter(brand__icontains=search)

    else:
        beverages = Beverage.objects.all()
    context = {
        'object_list':beverages,
    }

    return render(request, 'beverages/beverages-list.html', context=context)

class BeveragesListView(ListView):
    model = Beverage
    template_name = 'beverages/beverages-list.html'
    queryset = Beverage.objects.filter(sold = False)