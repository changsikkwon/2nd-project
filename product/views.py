import json

from django.views           import View
from django.http            import JsonResponse
from django.db.models       import Prefetch
from django.core.exceptions import ObjectDoesNotExist
from django.db.models       import Q

import re
from .models                import (
    MainCategory,
    SubCategory,
    TypeCategory,
    TypeCategoryProduct,
    Product,
    Image,
    HtmlTag,
    Description,
    Precaution,
    Size,
    Ingredient,
    Tag
)
from django.core.paginator  import Paginator

class ProductListView(View):
    def product_type_list(self, q, main_category, sub_category, type_category): #이거 같은 경우 type 카테고리 보기 
        products = Product.objects.filter(q)
        return [
        {
            "main_category": main_category,
            "sub_category" : sub_category,
            "type_category": type_category,
            "id"           : product.id,
            "korean_name"  : product.korean_name,
            "image"        : [ item.image_url for item in product.image_set.all()],
            "tag"          : [ item.tag for item in product.tag_set.all()]
        } 
        for product in products]

    def product_sub_list(self, q, main_category, sub_category): #sub 카테고리 전체보기
        products = Product.objects.filter(q)
        return [
        {
            "main_category" : main_category,
            "sub_category " : sub_category,
            "id"            : product.id,
            "korean_name"   : product.korean_name,
            "image"        : [ item.image_url for item in product.image_set.all()],
            "tag"          : [ item.tag for item in product.tag_set.all()]
        }
        for product in products]

    def product_all_list(self, q, main_category): #스킨케어 전체보기
        products = Product.objects.filter(q)
        return [
        {
            "main_category" : main_category,
            "id"            : product.id,
            "korean_name"   : product.korean_name,
            "image"        : [ item.image_url for item in product.image_set.all()],
            "tag"          : [ item.tag for item in product.tag_set.all()]
        }
        for product in products]

    def get(self, request):
        current_page = request.GET.get('page', 1) 

        sub_id = request.GET.get('sub', None) 
        type_id = request.GET.get('type',None) 

        main_category = SubCategory.objects.prefetch_related('main_category').values('main_category__name')
        
        #type_list
        if type_id != None:      
            sub_category = ""

            sub = TypeCategory.objects.filter(pk=type_id).prefetch_related('sub_category').values('sub_category__name') 
            sub_category = sub.first()['sub_category__name']
            type_category = TypeCategory.objects.get(pk=type_id)
            filtering = TypeCategoryProduct.objects.filter(type_category = type_id).values('product_id')
            objects = self.product_type_list(  Q  (pk__in=filtering), main_category.first()['main_category__name'], sub_category, type_category.name)          
            paging = Paginator(objects, 16) 
            return JsonResponse({'tot_page' : paging.num_pages,'data' : list(paging.get_page(current_page))}, status = 200)
        
        #sub_list
        elif sub_id != None:
            print("sub의 전체보기 , 유형별, 라인별, 고민별")
            sub_category = SubCategory.objects.get(pk=sub_id).name
            type_categories = TypeCategory.objects.filter(sub_category = sub_id).values('id') 
            filtering = TypeCategoryProduct.objects.filter(type_category_id__in = type_categories).values('product_id')
            objects = self.product_sub_list(  Q  (pk__in=filtering), main_category.first()['main_category__name'], sub_category)       
            paging = Paginator(objects, 16) 
            return JsonResponse({'tot_page' : paging.num_pages,'data' : list(paging.get_page(current_page))}, status = 200)

        #all_list
        elif sub_id == None and type_id == None:
            objects = self.product_all_list(Q(), main_category.first()['main_category__name'])
            paging = Paginator(objects, 16) 
            return JsonResponse({'tot_page' : paging.num_pages,'data' : list(paging.get_page(current_page))}, status = 200)

        return JsonResponse({'message' : 'Bad Request'}, status = 400)

class ProductDetailView(View):         
    def product_detail(self, q, main_category, sub_category, type_category):
        products = Product.objects.filter(q)
        return [
            {
                "product_id"    : product.id,
                "main_category" : main_category,
                "sub_category"  : sub_category,
                "type_category" : type_category,
                "korean_name"   : product.korean_name,
                "english_name"  : product.english_name,
                "size"          : product.size_set.first().size,
                "price"         : round(product.price),
                "image"         : [ item.image_url for item in product.image_set.all()],
                "tag"           : [ item.tag for item in product.tag_set.all()],
                "detail"        : product.htmltag_set.first().detail,
                "precaution"    : product.precaution_set.first().precaution,
                "ingredient"    : product.ingredient.ingredient,
                "description"   : product.description_set.first().description
            }
        for product in products]    

    def get(self, request, product_id):
        
        if Product.objects.filter(pk= product_id).exists():

            sub_id = request.GET.get('sub', None) 
            type_id = request.GET.get('type',None)

            main_category = SubCategory.objects.prefetch_related('main_category').values('main_category__name')

            sub_category=""
            type_category=""

            if type_id != None:
                type_category = TypeCategory.objects.get(pk=type_id).name
                sub_categories = TypeCategory.objects.filter(pk=type_id).prefetch_related('sub_category_set').values('sub_category__name')
                sub_category = sub_categories.first()['sub_category__name']

            elif sub_id != None:
                type_categories = TypeCategoryProduct.objects.filter(product_id = product_id).values('type_category_id')
                default_type_id = TypeCategory.objects.filter(pk__in = type_categories,sub_category = sub_id).values('id', 'name')
                type_id = default_type_id.first()['id']
                type_category = default_type_id.first()['name']
                sub_category = SubCategory.objects.get(pk=sub_id).name

            elif sub_id == None and type_id == None:
                type_categories = TypeCategoryProduct.objects.filter(product_id = product_id).values('type_category_id')
                default_type_id = TypeCategory.objects.filter(pk__in = type_categories,sub_category = 1).values('id', 'name')
                type_id = default_type_id.first()['id']
                type_category = default_type_id.first()['name']
                sub_categories = TypeCategory.objects.filter(pk=type_id).prefetch_related('sub_category_set').values('sub_category__name')
                print(sub_categories.first()['sub_category__name'])
                sub_category = sub_categories.first()['sub_category__name']

            return JsonResponse({'data' : self.product_detail(Q (pk=product_id), main_category.first()['main_category__name'], sub_category, type_category)}, status = 200)

        return JsonResponse({'message':"Product Does Not Exist"}, status = 400)

# 프론트에 타입별 id값을 따로 보내주고 그 id값으로 카테고리별 요청할때 쿼리스트링에 type id, sub id값을 쓸때 쓰라고 만듦
class ProductTypeListView(View):
    def type_list(self, q, main_category):
        typecategories = TypeCategory.objects.filter(q)
        return [
            {
                "main_category"     : main_category,
                "sub_category_id"   : typecategory.sub_category.id,
                "sub_category"      : typecategory.sub_category.name,
                "type_category_id"  : typecategory.id,
                "type_category"     : typecategory.name   
            }
        for typecategory in typecategories]    

    def get(self, request):
        try:
            main_category = SubCategory.objects.prefetch_related('main_category').values('main_category__name')

            return JsonResponse({'data': self.type_list(Q(), main_category.first()['main_category__name'])},status=200)
        except:
            return JsonResponse({'message':"Bad Request"}, status = 400)

class ProductSearchView(View):
    def searchProduct(self, q):
        products = Product.objects.filter(q)
        return [
            {
                "id"           : product.id,
                "korean_name"  : product.korean_name,
                "image"        : [ item.image_url for item in product.image_set.all()],
                "tag"          : [ item.tag for item in product.tag_set.all()]
            } 
        for product in products]

    def get(self, request):
        keyword     = request.GET.get('keyword', None)
        try:
            return JsonResponse({'data' : self.searchProduct(Q (korean_name__icontains = keyword) | Q (english_name__icontains = keyword))}, status = 200)
        except:
            return JsonResponse({'message' : 'No Search Result'}, status = 404)