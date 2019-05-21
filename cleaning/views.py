from django.shortcuts import render
from django.views import generic
from .models import Product


def main(request):
    return render(request,'cleaning/home.html')

def about(request):
    return render(request,'cleaning/aboutus.html')

def contact(request):
    return render(request,'cleaning/contactus.html')


class IndexViewPro(generic.ListView):
    template_name = 'cleaning/products.html'
    context_object_name = 'all_products'

    def get_queryset(self):
        return Product.objects.all()


class DetailViewPro(generic.DetailView):
    model = Product
    template_name ='cleaning/detailview.html'


def buynow(request):
    return render(request,'cleaning/buynow.html')

def product2(request):
    return render(request,'cleaning/product2.html')


