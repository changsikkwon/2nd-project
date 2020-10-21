import json
import re

from django.views       import View
from django.http        import JsonResponse

from user.models        import User
from product.models     import Product, Image
from .models            import Order, OrderItem
from user.utils         import login_required

class CartView(View):
    @login_required
    def post(self, request):
        data = json.loads(request.body)
        try:          
            order = Order.objects.create(
                user     = request.user,
            )
            
            OrderItem.objects.create(
                product_id = data['product'],
                quantity   = data['quantity'],
                order      = order
            )
            
            return JsonResponse({'message' : 'CART_ADDED'}, status = 200)
            
        except KeyError:    
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
            
    @login_required
    def get(self,request):
        try:
            items = OrderItem.objects.select_related('order', 'product').filter(order__user = request.user.id)
            
            product_list = [{
                'order_id'   : item.id,
                'product_id' : item.product.id,
                'name'       : item.product.korean_name,
                'image_url'  : item.product.image_set.first().image_url,
                'price'      : round(item.product.price),
                'quantity'   : item.quantity
            } for item in items]
        
            return JsonResponse({"product_list" : product_list}, status = 200)
        
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        
        except OrderItem.DoesNotExist:
            return JsonResponse({"message" : "EMPTY_CART"}, status = 404)
        
    @login_required
    def put(self, request):
        data = json.loads(request.body)   
        order = OrderItem.objects.get(order__user = request.user.id, id = data['order_id']) 
        order.quantity = data['quantity']
        order.save()
        
        product_list = [{
                'order_id'   : order.id,
                'product_id' : order.product.id,
                'name'       : order.product.korean_name,
                'image_url'  : order.product.image_set.first().image_url,
                'price'      : round(order.product.price),
                'quantity'   : order.quantity
        }]
        
        return JsonResponse({"product_list" : product_list}, status = 200)
    
    @login_required
    def delete(self, request):
        try:
            data = json.loads(request.body)
            order = OrderItem.objects.get(order__user = request.user, id = data['order_id'])  
            order.delete()
            order.order.delete()
            
            return JsonResponse({"product_list" : []}, status = 200)
        
        except:
            return JsonResponse({"message" : "NOT_EXIST_ORDER"}, status = 400)