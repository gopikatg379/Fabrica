from django.db import models
from Adminapp.models import Clothes, Register


# Create your models here.
class WishList(models.Model):
    wishlist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    cloth = models.ForeignKey(Clothes, on_delete=models.CASCADE)

    class Meta:
        db_table = 'wish_list_table'
