from django.shortcuts import render, redirect
from Adminapp.models import Clothes,CategoryCloth,SubCategoryCloth


# Create your views here.
def merchant_home(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        return render(request, 'merchant_home.html', {'user': user_id})
    else:
        return redirect('/')


def add_products(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        category = CategoryCloth.objects.get(categoryCloth_id=request.POST.get('category'))
        sub_category = SubCategoryCloth.objects.get(category_id=request.POST.get('subcategory'))
        stock = request.POST.get('stock')
        category_obj = Clothes(
            name = name,
            price=price,
            description=description,
            image= image,
            category= category,
            sub_category=sub_category,
            stock=stock
        )

        category_obj.save()
        return redirect('/merchant/add')
    category = CategoryCloth.objects.all()
    sub_category = SubCategoryCloth.objects.all()
    return render(request, 'add_products.html', {'category': category,'sub_category': sub_category})