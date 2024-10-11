from django.shortcuts import render
from .models import Products
# 1- adding paginator
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    products_list = Products.objects.all()
       # getting the search key typed
    product_name = request.GET.get('product_name')
    
    if product_name != '' and product_name is not None:
      #  products_list =  products_list.filter(title=movie_name)  # this line search the exact word because of "name" parameter,which is one of the attributes of the model,  to optimize, let's use the below code
        products_list = products_list.filter(title__icontains=product_name) # here we have double underscore "__" after title attribute to make the search less lenient 
    # setting up pagination
    paginator = Paginator(products_list, 4)  # this means four objects per page
    page = request.GET.get('page')  # getting the current page number ; remember "page" is the variable set in the  <a> of index.html
    # list of the movies of the current page
    products_list = paginator.get_page(page)
    context = {
        'products_list': products_list,
    }
    return render(request, 'shop/index.html',context)


def detail(request, product_id):
   product = Products.objects.get(id=product_id)
   context = {
       'product': product,
   }
   # return HttpResponse("This is item no/id %s" %item_id)
   return render(request, 'shop/detail.html', context)
