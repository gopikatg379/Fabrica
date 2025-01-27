from django.shortcuts import render, redirect
from Adminapp.models import Clothes, CategoryCloth, SubCategoryCloth,Sizes,Register
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def merchant_home(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        user = Register.objects.get(register_id=user_id)
        clothes = Clothes.objects.filter(user=user)

        paginator = Paginator(clothes, 6)
        page_number = request.GET.get('page')
        clothes_page = paginator.get_page(page_number)

        return render(request, 'merchant_home.html', {'user': user,'cloth':clothes_page})
    else:
        return redirect('/')


def add_products(request):
    if 'user_id' in request.session:
        user = Register.objects.get(register_id=request.session['user_id'])
        if user.categoryUser.categoryUser_name != 'Merchant':
            messages.error(request, 'You do not have permission to add products.')
            return redirect('/user/home')
        if request.method == 'POST':
            name = request.POST.get('name')
            price = request.POST.get('price')
            description = request.POST.get('description')
            image = request.FILES.get('image')
            category_id = request.POST.get('category')
            subcategory_id = request.POST.get('subcategory')
            stock = request.POST.get('stock')

            # Fetch category object
            try:
                category = CategoryCloth.objects.get(categoryCloth_id=category_id)
            except CategoryCloth.DoesNotExist:
                return JsonResponse({'error': 'Invalid category selected'}, status=400)

            # Fetch subcategory object (if provided)
            sub_category = None
            if subcategory_id:
                try:
                    sub_category = SubCategoryCloth.objects.get(category_id=subcategory_id)
                except SubCategoryCloth.DoesNotExist:
                    return JsonResponse({'error': 'Invalid subcategory selected'}, status=400)

            # Save the product
            category_obj = Clothes(
                user=user,
                name=name,
                price=price,
                description=description,
                image=image,
                category=category,
                sub_category=sub_category,
                stock=stock,
            )
            category_obj.save()

            selected_size = request.POST.getlist('sizes')

            for size_ids in selected_size:
                size = Sizes.objects.get(size_id=size_ids)
                category_obj.size.add(size)

            return redirect('/merchant/home')

        if request.method == 'GET' and 'gender' in request.GET:
            gender = request.GET.get('gender')
            categories = CategoryCloth.objects.filter(categoryGender=gender)
            category_list = [{'id': cat.categoryCloth_id, 'name': cat.CategoryCloth_name} for cat in categories]
            return JsonResponse({'categories': category_list})


        # Handle GET request for dynamic subcategories
        if request.method == 'GET' and 'category_id' in request.GET:
            category_id = request.GET.get('category_id')
            sub_categories = SubCategoryCloth.objects.filter(subcategory=category_id)
            sub_category_list = [{'id': sub.category_id, 'name': sub.subcategory_name} for sub in sub_categories]
            return JsonResponse({'subcategories': sub_category_list})

        # Render the form
        category = CategoryCloth.objects.all()
        sub_category = SubCategoryCloth.objects.all()
        sizes = Sizes.objects.all()
        return render(request, 'add_products.html', {'category': category, 'sub_category': sub_category, 'sizes': sizes})
    else:
        return redirect('/')


def delete_product(request,id):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        user = Register.objects.get(register_id=user_id)
        if user.categoryUser.categoryUser_name!= 'Merchant':
            messages.error(request, 'You do not have permission to delete products.')
            return redirect('/user/home')

        try:
            cloth = Clothes.objects.get(cloth_id=id)
            cloth.delete()
            messages.success(request, 'Product deleted successfully.')
        except Clothes.DoesNotExist:
            messages.error(request, 'Product not found.')

        return redirect('/merchant/home')
    else:
        return redirect('/login')


