from django.db import models
from django.core.validators import MinValueValidator


class Product_test(models.Model):
    title = models.CharField(max_length=63)


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    attributes = models.JSONField(blank=True, null=True)


class Manufacturer(models.Model):
    name = models.CharField(max_length=127, unique=True)


class Image(models.Model):
    image = models.ImageField(upload_to='product/', null=True, blank=True)
    description = models.TextField(blank=True, null=True)


class Product(models.Model):
    QUALITY_CHOICES = [
        ('FACTORY', 'Factory-sealed'),
        ('O_BOX', 'Open-box'),
        ('REFURBSH', 'Refurbished'),
        ('USED', 'Used'),
        ('DEFECTD', 'Defected'),
        ('NONE', 'Not-listed')
    ]


    title = models.CharField(max_length=255)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    quality = models.CharField(max_length=15, choices=QUALITY_CHOICES, default='NONE')
    product_image = models.ManyToManyField(Image, related_name='products', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, related_name='products')
    seller = models.ForeignKey("profiler.Profile", on_delete=models.CASCADE, related_name='products')