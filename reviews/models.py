from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    title = models.CharField(max_length=127)
    rating = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    description = models.TextField()
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey('profiler.Profile', on_delete=models.DO_NOTHING, related_name='reviews')

    def __str__(self):
        return f'{self.rating} stars. Review for {self.product.name} by {self.reviewer.user.username}'