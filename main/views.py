from django.shortcuts import render
from .models import Category,Product
from django.shortcuts import render, get_object_or_404
from mail_sending.forms import ContactModelForm
from django.http import JsonResponse
from cart.forms import CartAddProductForm
from cart.cart import Cart
# Create your views here.
def index(request):
    form = ContactModelForm()
    if request.is_ajax():
        form = ContactModelForm(request.POST)
        print(request.POST)

        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'success'
            })
    return render(request, 'main.html',{"categories": Category.objects.all(),'form': form})

def category_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.get_products.order_by('id')
    return render(request, 'catalog page.html',{"products": products})

def item_view(request, name, slug):
    product = Product.objects.get(slug=slug)
    cart_product_form = CartAddProductForm()
    return render(request, 'product card.html', {'product': product,'cart_product_form': cart_product_form})