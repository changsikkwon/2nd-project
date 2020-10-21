import os, sys ,csv , django, pandas as pd

from product.models         import (
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

import re
from ast                    import literal_eval

def run():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hyunlanege.settings")
    django.setup()
    CSV_PATH = '/Users/cs/hyunlaneige/11-Hyunlaneige-backend/scripts/product_200908.csv'
    with open(CSV_PATH) as in_file:
        data_reader = csv.reader(in_file)
    data = pd.read_csv(CSV_PATH,converters = {
        "sub_category" : literal_eval,
        "type_category" : literal_eval,
        "tag" : literal_eval,
        "image_url" : literal_eval
        })

    for _, row in data.iterrows():

        main_category, created = MainCategory.objects.get_or_create(
            name = row['main_category'],
        )
        for sub_category in row['sub_category']: 
            sub_category, created = SubCategory.objects.get_or_create(
                name                = sub_category,
                main_category       = main_category
            )
     
        for index in range(len(row['type_category'])):
            row['type_category'][index], created = TypeCategory.objects.get_or_create(
                name = row['type_category'][index],
                sub_category = SubCategory.objects.get(name=row['sub_category'][index])
            )

        product, created = Product.objects.get_or_create( 
            korean_name     = row['koran_name'],
            english_name    = row['english_name'],
            price           = row['price'][:-1].replace(",",""),
        )
        for type_category in row['type_category']:
            typecategoryproduct, created = TypeCategoryProduct.objects.get_or_create(
                type_category         = type_category,
                product               = product 
        )
        for image in row['image_url']:
            image, created = Image.objects.get_or_create(
                image_url  = image,
                product    = product
            )

        htmltag, created = HtmlTag.objects.get_or_create(
            detail  = row['detail'],
            product = product
        )
        description, created = Description.objects.get_or_create(
            description   = row['description'],
            product       = product
        )
        precaution, created = Precaution.objects.get_or_create(
            precaution    = row['precaution'],
            product       = product
        )
        size, created = Size.objects.get_or_create(
            size          = row['size'],
            product       = product
        )
        ingredient, created = Ingredient.objects.get_or_create(
            ingredient    = row['ingredient'],
            product       = product
        )

        for tag in row['tag']:
            tag, created   = Tag.objects.get_or_create(
                tag        = tag,
                product    = product
            )

            