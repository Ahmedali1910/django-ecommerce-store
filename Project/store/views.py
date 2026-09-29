from django.shortcuts import render , redirect ,get_object_or_404
from .forms import ProductForm
from .models import Product,Category
from decimal import Decimal

# Create your views here.
def home (request):
    return render(request,'store/home.html')

def products(request):
    products=Product.objects.all()
    return render(request,"store/Product_List.html",{"products":products})

def details(request,id):
    product=get_object_or_404(Product,id=id)
    return render(request,"store/Product_Details.html",{"product":product})

def categorize(request,id):
    category=get_object_or_404(Category,id=id)
    products=Product.objects.filter(category=category)
    return render(request,"store/Category_Product.html",{"products":products,"category":category})

def  search_by_price (request,price):
    price=Decimal(price)
    products=Product.objects.filter(price__gt=price)
    return render(request,"store/search.html",{"products":products,"price":price})

def create (request):
    if request.method== "POST" :
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect ("product_list")
    else:
        form=ProductForm()

    return render(request,'store/Create_Product.html',{"form":form,"message":"Create"})   


def edit (request,id):
    product=get_object_or_404(Product,id=id)
    if request.method== "POST" :
            form=ProductForm(request.POST,instance=product)
            if form.is_valid():
                form.save()
                return redirect("product_details",id=id)
    else:
       form=ProductForm(instance=product)

    return render(request,'store/Create_Product.html',{"form":form,"message":"Edit"})      

def delete(request,id):
    product=get_object_or_404(Product,id=id)
    product.delete()
    return redirect("product_list") 


def category_list(request):
    categories=Category.objects.all()
    return render(request,'store/category_list.html',{"categories":categories})
