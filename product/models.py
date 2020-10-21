from django.db          import models

from user.models        import User

class MainCategory(models.Model):
    name         = models.CharField(max_length = 32)
    class Meta:
        db_table = "main_categories"
        
#서브 카테고리테이블
class SubCategory(models.Model):
    name          = models.CharField(max_length = 64)
    main_category = models.ForeignKey('MainCategory', on_delete = models.CASCADE)
    
    class Meta:
        db_table = "sub_categories"
        
#종류 카테고리테이블
class TypeCategory(models.Model):
    name          = models.CharField(max_length = 100)
    sub_category  = models.ForeignKey('SubCategory', on_delete = models.CASCADE)
    
    class Meta:
        db_table = "type_categories"

class TypeCategoryProduct(models.Model):
    type_category = models.ForeignKey('TypeCategory', on_delete = models.CASCADE)
    product       = models.ForeignKey('Product', on_delete = models.CASCADE)  

class Product(models.Model):
    korean_name    = models.CharField(max_length = 64)
    english_name   = models.CharField(max_length = 64)
    price          = models.DecimalField(max_digits = 10, decimal_places = 2)
    type_category  = models.ManyToManyField(TypeCategory, through = TypeCategoryProduct)

    class Meta:
        db_table = "products"

class Image(models.Model):
    image_url  = models.URLField(max_length = 2048, null = True)
    product    = models.ForeignKey(Product, on_delete = models.CASCADE)
    
    class Meta:
        db_table = "images"
        
#html 테이블
class HtmlTag(models.Model):
    detail     = models.TextField()
    product    = models.ForeignKey(Product, on_delete = models.CASCADE)
    
    class Meta:
        db_table = "html_tags"     
           
#설명 테이블
class Description(models.Model):
    description = models.TextField(null = True)
    product     = models.ForeignKey(Product, on_delete = models.CASCADE)
    
    class Meta:
        db_table = "descriptions"
        
#주의사항 테이블
class Precaution(models.Model):
    precaution = models.TextField()
    product    = models.ForeignKey(Product, on_delete = models.CASCADE)
    
    class Meta:
        db_table = "precautions"
        
#사이즈 테이블
class Size(models.Model):
    size    = models.CharField(max_length = 128)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)

    class Meta:
        db_table = "sizes"
        
#전성분 테이블
class Ingredient(models.Model):
    ingredient = models.TextField()
    product    = models.OneToOneField(Product, on_delete = models.CASCADE)
    
    class Meta:
        db_table = "ingredients"
        
#태그 테이블
class Tag(models.Model):
    tag     = models.CharField(max_length = 64)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    
    class Meta:
        db_table = "tags"