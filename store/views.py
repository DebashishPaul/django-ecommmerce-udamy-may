from django.shortcuts import render
from .models import Product, Order
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

def CheckoutView(request):
    if request.method == 'POST':
        item = request.POST.get('item', "")
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"")
        order = Order(item=item, name=name, email=email, address=address, city=city, zipcode=zipcode, total=total)
        order.save()
    return render(request, 'store/checkout.html')