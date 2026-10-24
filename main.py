from products.models import *
img = Image.objects.get(id=1)
print(img.products.all())   # должны быть продукты
