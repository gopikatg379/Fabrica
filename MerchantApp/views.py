from django.shortcuts import render, redirect
from Adminapp.models import Clothes, CategoryCloth, SubCategoryCloth
from django.http import JsonResponse


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
            name=name,
            price=price,
            description=description,
            image=image,
            category=category,
            sub_category=sub_category,
            stock=stock
        )
        category_obj.save()
        return redirect('/merchant/add')

    if request.method == 'GET' and 'category_id' in request.GET:
        category_id = request.GET.get('category_id')
        sub_categories = SubCategoryCloth.objects.filter(subcategory=category_id)
        sub_category_list = [
            {'id': sub.category_id, 'name': sub.subcategory_name} for sub in sub_categories
        ]
        return JsonResponse({'subcategories': sub_category_list})

    category = CategoryCloth.objects.all()
    sub_category = SubCategoryCloth.objects.all()
    return render(request, 'add_products.html', {'category': category, 'sub_category': sub_category})





