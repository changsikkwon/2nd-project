from django.db import models

class Review(models.Model):
    product         = models.ForeignKey('product.Product', on_delete = models.CASCADE)
    user            = models.ForeignKey('user.User', on_delete = models.CASCADE)
    rating          = models.DecimalField(max_digits = 2, decimal_places = 1)
    skin_type       = models.CharField(max_length = 32)
    created_at      = models.DateTimeField(auto_now_add = True)
    updated_at      = models.DateTimeField(auto_now = True)
    comment         = models.TextField()
    review_image    = models.URLField(max_length = 1024, blank = True, null = True)
    
    class Meta:
        db_table    = 'reviews'