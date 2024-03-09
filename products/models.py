from django.db import models


# Sozdayom model dlya kategoriy
class CategoryModel(models.Model):
    title = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# Sozdayom model dlya produkta
class ProductModel(models.Model):
    product_title = models.CharField(max_length=50)
    product_price = models.FloatField()
    product_description = models.TextField()
    product_amount = models.IntegerField()
    product_image = models.ImageField(upload_to='products')
    product_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    product_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class CartModel(models.Model):
    user_id = models.IntegerField()
    user_product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    user_product_quantity = models.IntegerField()
    user_add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_id)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
