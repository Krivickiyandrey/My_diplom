from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404
from django.db.models import ObjectDoesNotExist
from MotoMarket.models import Sportbike, Cruiser, Enduro, Quadro
from django.apps import apps

moto_models = {
    "Cruiser": Cruiser,
    'Sportbike': Sportbike,
    'Enduro': Enduro,
    'Quadro': Quadro
}


def index(request):
    context = {'message': 'Выбери интересующую категорию'}
    return render(request, 'index.html', context)


def moto_list(request, moto_type):
    if request.method == 'GET':
        model = moto_models.get(moto_type)
        list = model.objects.all()
        context = {'bikes_list': list}
        return render(request, 'moto_list.html', context)


def moto_detail(request, moto_type, pk):
    model = moto_models.get(moto_type)
    moto = get_object_or_404(model, id=pk)

    context = {'moto': moto}
    return render(request, 'moto_detail.html', context)


# def SB(request):
#     if request.method == 'GET':
#         list = Sportbike.objects.all()
#         context = {'SportbikeList': list}
#         return render(request, 'SB.html', context)
#
#
# def Cruisers(request):
#     if request.method == 'GET':
#         list = Cruiser.objects.all()
#         context = {'cruiserList': list}
#         return render(request, 'Cruisers.html', context)
#
#
# def Enduros(request):
#     if request.method == 'GET':
#         list = Enduro.objects.all()
#         context = {'enduroList': list}
#         return render(request, 'Enduros.html', context)
#
#
# def quadros(request):
#     if request.method == 'GET':
#         list = Quadro.objects.all()
#         context = {'quadroList': list}
#         return render(request, 'Quadros.html', context)
#
#
# def find_SB(request, sportbike_id):
#     sportbike = Sportbike.objects.get(id=sportbike_id)
#     if sportbike is None:
#         raise Http404(f'Sportbike "{sportbike_id}" not found')
#
#     context = {'sportbike': sportbike}
#     return render(request, 'the_SB.html', context)
#
#
# def find_Cruiser(request, cruiser_id):
#     cruiser = Cruiser.objects.get(id=cruiser_id)
#     if cruiser is None:
#         raise Http404(f'Cruiser "{cruiser_id}" not found')
#     context = {'cruiser': cruiser}
#     return render(request, 'the_Cruiser.html', context)
#
#
# def find_Enduro(request, enduro_id):
#     enduro = Enduro.objects.get(id=enduro_id)
#     if enduro is None:
#         raise Http404(f'Enduro "{enduro_id}" not found')
#     context = {'enduro': enduro}
#     return render(request, 'the_Enduro.html', context)
#
#
# def find_Quadro(request, quadro_id):
#     quadro = Quadro.objects.get(id=quadro_id)
#     if quadro is None:
#         raise Http404(f'Quadro "{quadro_id}" not found')
#     context = {'quadro': quadro}
#     return render(request, 'the_Quadro.html', context)


def add_to_cart_moto(request, moto_type, pk):
    item = moto_type + '_' + str(pk)
    if 'cart' not in request.session.keys():
        request.session['cart'] = list()
    if item not in request.session['cart']:
        updated_cart = request.session['cart']
        updated_cart.append(item)
        request.session['cart'] = updated_cart
    return redirect('moto_list', moto_type=moto_type)


def shopping_cart(request):
    cart_list = []
    if 'cart' not in request.session.keys():
        return render(request, 'Cart.html', {"cart_list": cart_list})
    cart = request.session['cart']
    for item in cart:
        model, id = item.split('_')
        model = moto_models.get(model)
        try:
            obj = model.objects.get(id=id)
            cart_list.append(obj)
        except ObjectDoesNotExist:
            continue
    return render(request, 'Cart.html', {"cart_list": cart_list})


def delete_from_cart_moto(request, moto_type, pk):
    item = moto_type + '_' + str(pk)
    if 'cart' in request.session.keys() and item in request.session['cart']:
        updated_cart = request.session['cart']
        updated_cart.remove(item)
        request.session['cart'] = updated_cart

    return redirect('cart_detail')

def deal(request, moto_type, pk):
    item = moto_type + '_' + str(pk)
    if 'cart' in request.session.keys() and item in request.session['cart']:
        updated_cart = request.session['cart']
        updated_cart.remove(item)
        request.session['cart'] = updated_cart
        model = apps.get_model(app_label='MotoMarket', model_name=moto_type)
        model.objects.filter(id=pk).delete()
    return render(request, 'deal.html')

def sort_by_country(request, country_id):
    list_cruisers = list(Cruiser.objects.filter(country_id=country_id))
    list_SBs = list(Sportbike.objects.filter(country_id=country_id))
    list_enduros = list(Enduro.objects.filter(country_id=country_id))
    list_quadro = list(Quadro.objects.filter(country_id=country_id))
    general_list = list_quadro + list_SBs + list_cruisers + list_enduros
    return render(request, 'moto_list.html', {'bikes_list': general_list})
