from django.shortcuts import render,get_object_or_404,redirect,redirect
from . models import Product, Cart
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "password do not match")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "username already exist")


        User.objects.create_user(
            username=username,
            email=email,
            password=password

        )
        messages.success(request, "account created successfully")
        return redirect("login")

    return render(request, "includes/register.html")


def user_login(request):
    
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect("home")

        messages.error(request, "Invalid username or password.")

    return render(request, "includes/login.html")

def user_logout(request):
    logout(request)
    return redirect("home")