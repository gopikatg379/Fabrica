from django.contrib import admin
from .models import CategoryCloth,CategoryUser,CategoryGender,SubCategoryCloth,Sizes
# Register your models here.

admin.site.register(CategoryCloth)
admin.site.register(CategoryUser)
admin.site.register(CategoryGender)
admin.site.register(SubCategoryCloth)
admin.site.register(Sizes)
