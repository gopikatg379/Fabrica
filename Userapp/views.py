from django.shortcuts import render, redirect
from Adminapp.models import CategoryGender, Register, Clothes, Cart
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
        cart_obj = Cart.objects.filter(user=user_id)
        total_price = sum(item.total_price for item in cart_obj)
        delivery_tax = 2
        discount = 40
        coupon_discount = 10
        grand_total = total_price + delivery_tax - discount - coupon_discount
        if grand_total < 0:
            grand_total = 0
        else:
            grand_total = grand_total
        return render(request, 'user_cart.html',
                      {'user': user_id, 'data': cart_obj, 'total': total_price, 'delivery_tax': delivery_tax,
                       'discount': discount,
                       'coupon_discount': coupon_discount, 'grand_total': grand_total})
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
            return redirect('/user/home')
        except WishList.DoesNotExist:
            wish_obj = WishList(
                user=user_id,
                cloth=cloth_obj
            )
            wish_obj.save()
            return redirect('/user/home')
    else:
        return redirect('/login')


def view_more(request, id):
    cloth_obj = Clothes.objects.get(cloth_id=id)
    print(cloth_obj.size)
    sizes = cloth_obj.size.all()
    print(sizes)
    return render(request, 'view_more.html', {'data': cloth_obj,'sizes': sizes})


def add_cart(request, id):
    if 'user_id' in request.session:
        cloth_obj = Clothes.objects.get(cloth_id=id)
        user = Register.objects.get(register_id=request.session['user_id'])
        try:
            cart_obj = Cart.objects.get(cloth=cloth_obj, user=user)
            quantity_change = request.GET.get('quantity', None)
            if quantity_change == 'decrease' and cart_obj.quantity > 1:
                cart_obj.quantity -= 1
            else:
                cart_obj.quantity += 1

            cart_obj.save()
            return redirect('/user/cart')
        except Cart.DoesNotExist:
            cart_obj = Cart(cloth=cloth_obj, user=user)
            cart_obj.save()
            return redirect('/user/cart')
    else:
        return redirect('/login')


def delete_cart(request, id):
    if 'user_id' in request.session:
        cart_obj = Cart.objects.get(cart_id=id)
        cart_obj.delete()
        return redirect('/user/cart')
