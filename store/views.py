from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.

def IndexView(request):
    product_query = Product.objects.all()
    get_name = request.GET.get('search_item')
    
    #search task
    if get_name is not None and get_name != '':
        product_query = product_query.filter(name__icontains=get_name)
    
    #pagination task
    paginator = Paginator(product_query, 4)
    page_number = request.GET.get('page')
    product_query = paginator.get_page(page_number)

    #context task
    context = {
        'product_query': product_query
    }

    return render(request, 'store/index.html', context)

def DetailsView(request, id):
    item = Product.objects.get(pk=id)
    return render(request, 'store/details.html',{'item':item})