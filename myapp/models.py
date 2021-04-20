from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Category'


class Products(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'
