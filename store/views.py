from django.shortcuts import render,get_object_or_404,redirect
from . models import Product, Cart
# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request,"store/home.html",{
        "products":products
    })
def products(request):
    products = Product.objects.all()
    return render(request, "includes/products.html",{
        "products":products
    })

def productDetails(request, id):
    product = get_object_or_404(Product,id=id)
    return render(request, 'includes/productDetails.html', {'product':product})

def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    cart_item, created = Cart.objects.get_or_create(
        product=product,
        defaults={"quantity": 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart")


def cart(request):
    cart_items = Cart.objects.all()

    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    return render(request, "includes/cart.html", {
        "cart_items": cart_items,
        "total": total
    })

def increase_quantity(request, id):
    cart_item = get_object_or_404(Cart,id=id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect("cart")

def decrease_quantity(request, id):
    cart_item = get_object_or_404(Cart, id=id)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect("cart")

def remove_cart(request, id):
    cart_item = get_object_or_404(Cart, id=id)
    cart_item.delete()
    return redirect("cart")