from django.db import models


# Create your models here.
class CategoryGender(models.Model):
    categoryGender_id = models.AutoField(primary_key=True)
    categoryGender_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'category_gender_table'


class CategoryCloth(models.Model):
    categoryCloth_id = models.AutoField(primary_key=True)
    CategoryCloth_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'category_cloth_table'


class SubCategoryCloth(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_gender = models.ForeignKey(CategoryGender, on_delete=models.CASCADE, null=True)
    subcategory = models.ForeignKey(CategoryCloth, on_delete=models.CASCADE, null=True)
    subcategory_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'sub_category_table'


class CategoryUser(models.Model):
    categoryUser_id = models.AutoField(primary_key=True)
    categoryUser_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'category_user_table'


class Register(models.Model):
    register_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=255, null=True)
    categoryUser = models.ForeignKey(CategoryUser, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/')

    class Meta:
        db_table = 'register_table'


class Clothes(models.Model):
    cloth_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='clothes_images/')
    category = models.ForeignKey(CategoryCloth, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategoryCloth, on_delete=models.CASCADE, null=True)
    stock = models.IntegerField()

    class Meta:
        db_table = 'cloth_table'
