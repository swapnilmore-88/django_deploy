from django.shortcuts import render, redirect
from product.models import Product
from django.http import HttpResponse
from product.forms import ProductForm


# Create your views here.
def get_product(id):#to get single product data
    return Product.objects.get(pk=id )


def get_products(request):
    all_products = Product.objects.all()  # its a query
    if all_products:
        return render(request, 'index.html', {'msg': 'welcome', 'all_products': all_products})
        # in django jinja variable are sent in dictionary
    return render(request, 'index.html', {'msg': 'No data is found', 'all_products': []})


def create_product(request):
    try :
        prod =  get_product(request.POST["pid"])# to get single data we use pk-primary key
        #here  request.POST["pid"] is a dictionary
    except : #to bypass key error
        prod = None

    if prod:#for editing existing product data
        form = ProductForm(request.POST, instance=prod)
        msg = "Product is Updated"
    else:#for adding new product data
        form = ProductForm(request.POST)  # creates a blank form when method is GET
        # if method is POSt then it will have some data
        msg = "Product is Added"
    if request.method == 'POST':
        print(form)
        if form.is_valid():
            form.save()  # here it will add it in database
            return render(request, 'index.html', {'msg': msg, 'all_products': Product.objects.all()})
        else:
            return render(request, 'edit.html', {'msg': form.errors, 'form': form})
    return render(request, 'edit.html', {'msg': 'please fill following details', 'form': form})


def update_product(request, id):
    prod = Product.objects.get(pk =id) # we can call get_product funtion here
    if prod:
        form = ProductForm(instance=prod)# here instance will provide data to create ProductForm
        return render(request,'edit.html',{"form":form})
    return redirect('get_all') # while redirecting we dont give name of rout.html ,
    # we just give name of url present in product.urls


def delete_product(request,id):
    prod = get_product(id)
    if prod:
        prod.delete()
        return render(request, "index.html", {"msg":"Product deleted successfully", "all_products": Product.objects.all()})

    return render(request, "index.html", {"msg":"Product NOT Found", "all_products":Product.objects.all()})

