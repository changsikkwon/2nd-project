import json

from django.core.paginator  import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.http            import JsonResponse
from django.views           import View

from user.models            import User
from product.models         import Product
from user.utils             import login_required
from .models                import Review
from datetime               import datetime

class ReviewView(View):
    @login_required
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            if Product.objects.filter(id = data['product_id']).exists():
                            
                Review.objects.create(
                    comment      = data['comment'],
                    rating       = data['rating'],
                    review_image = data['review_image'],
                    product_id   = data['product_id'],
                    user_id      = request.user.id,
                    skin_type    = data['skin_type'],
                )
                
                return JsonResponse({'message' : 'REVIEW_SUCCESS'}, status = 200)
            return JsonResponse({'message' : 'INVALID_PRODUCT'}, status = 400)
        
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        
    def get(self, request):
        product = request.GET.get('product', None)
        
        if product:
            review_list = [{
                'review_id'    : review.id,
                'identifier'   : review.user.identifier,
                'comment'      : review.comment,
                'rating'       : review.rating,
                'review_image' : review.review_image,
                'skin_type'    : review.skin_type,
                'date'         : review.created_at
            } for review in Review.objects.filter(product_id = product)]
            
            return JsonResponse({'Review_list' : review_list}, status = 200)
        return JsonResponse({'message' : 'INVALID_PRODUCT'}, status = 400)
        
    @login_required
    def delete(self, request):
        try:
            data = json.loads(request.body)
            
            Review.objects.get(id = data['review_id'], user = request.user).delete()
            
            return JsonResponse({'message' : 'DELETE_SUCCESS'}, status = 200)
        
        except Review.DoesNotExist:
            return JsonResponse({'message' : 'INVALID_REVIEW'}, status = 400)