from django.shortcuts import render, redirect
from Adminapp.models import CategoryGender, Register, Clothes
from .models import *


# Create your views here.
def user_home(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        user = Register.objects.get(register_id=user_id)
        return render(request, 'user_home.html', {'user': user})
    else:
        return redirect('/login')


def wishlist(request):
    if 'user_id' in request.session:
        cloth_obj = WishList.objects.filter(user=request.session['user_id'])
        return render(request, 'user_wishlist.html', {'data': cloth_obj})
    else:
        return redirect('/login')


def view_cart(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        return render(request, 'user_cart.html', {'user': user_id})
    else:
        return redirect('/login')


def logout(request):
    del request.session['user_id']
    return redirect('/')


def add_wishlist(request, id):
    if 'user_id' in request.session:
        user_id = Register.objects.get(register_id=request.session['user_id'])
        cloth_obj = Clothes.objects.get(cloth_id=id)
        try:
            wish_obj = WishList.objects.get(cloth=cloth_obj)
            wish_obj.delete()
            return redirect('/t-shirts')
        except WishList.DoesNotExist:
            wish_obj = WishList(
                user=user_id,
                cloth=cloth_obj
            )
            wish_obj.save()
            return redirect('/t-shirts')
    else:
        return redirect('/login')


def view_more(request, id):
    cloth_obj = Clothes.objects.get(cloth_id=id)
    return render(request, 'view_more.html', {'data': cloth_obj})
