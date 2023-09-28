from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .models import *


def count_cart(request):
    username = request.user.username
    cart_count = Cart.objects.filter(checkout = False, username = username).count()
    return cart_count


class BaseView(View):
    views = {}
    views['information'] = Information.objects.all()


class HomeView(BaseView):
    def get(self, request):
        self.views
        self.views["cart_counts"] = count_cart(request)
        self.views['abouts'] = About.objects.all()
        self.views['teams'] = Team.objects.all()
        self.views['review'] = Review.objects.all()
        self.views['special_img'] = MenuItemImage.objects.filter(labels='special')
        self.views['special_items'] = MenuItem.objects.filter(labels='special')
        for review in self.views['review']:
            review.star_list = range(review.star_rating)

        self.views['service'] = Service.objects.all()
        self.views['categories']= MenuCategory.objects.all()
        for category in self.views['categories']:
            category.items = MenuItem.objects.filter(category=category)
        return render(request, 'index.html', self.views)


def contact(request):
    views = {}
    views["cart_counts"] = count_cart(request)
    views['information'] = Information.objects.all()

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        data.save()
        messages.success(request, f"Dear {name}, Thanks for your time!")
        return redirect('contact')

    return render(request, 'contact.html', views)


class MenuView(BaseView):
    def get(self, request):
        self.views["cart_counts"] = count_cart(request)
        self.views['categories']= MenuCategory.objects.all()
        for category in self.views['categories']:
            category.items = MenuItem.objects.filter(category=category)
            category.image = MenuItemImage.objects.filter(category=category)
        return render(request, 'menu.html', self.views)


class AboutView(BaseView):
    def get(self, request):
        self.views
        self.views["cart_counts"] = count_cart(request)
        self.views['abouts'] = About.objects.all()
        self.views['teams'] = Team.objects.all()
        self.views['review'] = Review.objects.all()

        for review in self.views['review']:
            review.star_list = range(review.star_rating)

        return render(request, 'about.html', self.views)


class CartView(BaseView):

    def get(self, request):

        username = request.user.username
        self.views["cart_counts"] = count_cart(request)
        self.views['cart_view'] = Cart.objects.filter(username = username )
        s = 0
        for i in self.views["cart_view"]:
            s = s + i.total
        self.views["sub_total"] = s
        self.views['delevery_charge'] = 100
        self.views['grand_total'] = s+100

        return render(request, 'cart.html', self.views)


def add_to_cart(request, slug):
    username = request.user.username
    if MenuItem.objects.filter(slug=slug).exists():
        if Cart.objects.filter(slug=slug, checkout=False, username=username).exists():
            quantity = Cart.objects.get(slug=slug, checkout=False, username=username).quantity
            price = MenuItem.objects.get(slug=slug).price
            quantity = quantity + 1
            total = price * quantity
            Cart.objects.filter(slug=slug, checkout=False, username=username).update(total=total, quantity=quantity)
        else:
            price = MenuItem.objects.get(slug=slug).price
            total = price
            data = Cart.objects.create(
                username=username,
                slug=slug,
                total=total,
                quantity=1,
                items=MenuItem.objects.get(slug=slug),
                items_img = MenuItemImage.objects.get(slug=slug),
            )
            data.save()
    else:
        return redirect('/')

    return redirect('/cart')


def reduce_quantity(request, slug):
    username = request.user.username
    if MenuItem.objects.filter(slug=slug).exists():
        if Cart.objects.filter(slug=slug, checkout=False, username=username).exists():
            quantity = Cart.objects.get(slug=slug, checkout=False, username=username).quantity
            price = MenuItem.objects.get(slug=slug).price
            if quantity > 1:
                quantity = quantity - 1
            total = price * quantity
            Cart.objects.filter(slug=slug, checkout=False, username=username).update(total=total, quantity=quantity)
        else:
                messages.error(request, 'The quantity cannot be less than 1.')
    return redirect('/cart')


def delete_cart(request, slug):
    username = request.user.username
    if Cart.objects.filter(slug=slug, checkout=False, username=username).exists():
        Cart.objects.filter(slug=slug, checkout=False, username=username).delete()

        return redirect('/cart')


def signup(request):
    views = {}
    views['information'] = Information.objects.all()
    if request.method == "POST":
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'The username is already taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'The email is already used.')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                    password=password,
                )
                # messages.success(request, 'Sign up successful! Please log in.')
                return redirect('login')
        else:
            messages.error(request, 'The password does not match.')
    return render(request, 'signup.html',views )


def login_view(request):
    views = {}
    views['information'] = Information.objects.all()

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('login')

    return render(request, "login.html", views)


class CheckoutView(BaseView):
    def get(self, request):
            username = request.user.username
            self.views["cart_counts"] = count_cart(request)
            self.views['orders'] = Cart.objects.filter(username=username)
            s = 0
            for i in self.views["orders"]:
                s = s + i.total
            self.views["sub_total"] = s
            self.views['delivery_charge'] = 100
            self.views['grand_total'] = s + 100

            return render(request, 'checkout.html', self.views)



    @login_required
    def placeorder(request):
        if request.method == 'POST':
            # Retrieve data from the form
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            phone = request.POST['phone']
            address = request.POST['address']
            city = request.POST['city']
            total_price = 0

            if email != request.user.email:
                messages.error(request, 'Email does not match your account')
                return redirect('checkout')

            # Create a new order instance
            order = Order(
                fname=fname,
                lname=lname,
                email=email,
                phone=phone,
                address=address,
                city=city,
                total_price=total_price,
                status='Pending'
            )
            order.save()
            Cart.objects.filter(username=request.user.username).delete()

            return redirect('/')

        # If the request method is not POST, you may want to handle this case accordingly.
        return render(request, 'checkout')


def change_order_status(request, order_id, new_status):
    # Retrieve the order you want to update
    order = get_object_or_404(Order, id=order_id)

    try:
        # Use the update_status method to change the status
        order.update_status(new_status)
        messages.success(request, f'Order #{order_id} status changed to {new_status}')
    except ValueError as e:
        # Handle the case where an invalid status choice was provided
        messages.error(request, str(e))

    return redirect('/')



