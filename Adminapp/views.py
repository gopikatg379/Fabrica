from django.shortcuts import render, redirect
from .models import *
from Userapp.models import WishList


# Create your views here.
def register(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['address']
        category = CategoryUser.objects.get(categoryUser_id=request.POST['category'])
        print(category)
        image = request.FILES['profile_image']
        user = Register(
            name=username,
            email=email,
            password=password,
            phone=phone,
            address=address,
            categoryUser=category,
            profile_image=image,
        )
        user.save()
        return redirect('/login')
    category_obj = CategoryUser.objects.all()
    return render(request, 'register.html', {'categories': category_obj})


def login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = Register.objects.get(name=username, password=password)
            if user.categoryUser.categoryUser_name == 'Customer':
                request.session['user_id'] = user.register_id
                return redirect('user/home')
            elif user.categoryUser.categoryUser_name == 'Merchant':
                request.session['user_id'] = user.register_id
                return redirect('merchant/home')
        except Register.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


def home(request):
    return render(request, 'user_home.html')


def tshirt(request,id):
    if 'user_id' in request.session:
        sub_obj = Clothes.objects.filter(sub_category=id)
        reg_obj = Register.objects.get(register_id=request.session['user_id'])
        wishlist = WishList.objects.filter(user=reg_obj).values_list('cloth__cloth_id', flat=True)
        return render(request, 'tshirt.html', {'data': sub_obj, 'wishlist_ids': wishlist,'user':reg_obj})
    else:
        return redirect('/login')
