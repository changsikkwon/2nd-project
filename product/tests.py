import json

from django.test  import (
    TestCase,
    Client
)
from .models     import (
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

class ProductTest(TestCase):

    maxDiff = None

    def setUp(self):
        client = Client()

        ################# MainCategory #################
        MainCategory.objects.create(
            id   = 1,
            name = "스킨케어"
        )

        ################# SubCategory #################
        SubCategory.objects.create(
            id   =  1,
            name =  "유형별",
            main_category = MainCategory.objects.get(id=1)
        )

        ################# TypeCategory #################
        TypeCategory.objects.create(
            id = 1,
            name = "젤/크림",
            sub_category = SubCategory.objects.get(id=1)
        )

        ################# Product #################
        Product.objects.create(
            id           = 1,
            korean_name  = "퍼펙트 리뷰 유스 리제너레이팅 크림",
            english_name = "PERFECT RENEW YOUTH REGENERATING CREAM",
            price        = 65000
        )

        Product.objects.create(
            id           = 2,
            korean_name  = "래디언-C 크림",
            english_name = "RADIAN-C CREAM",
            price        = 29000
        )

        Product.objects.create(
            id           = 3,
            korean_name  = "워터뱅크 하이드로 크림 EX",
            english_name = "WATER BANK HYDRO CREAM EX",
            price        = 37000
        )

        ################# Product 와 TypeCategory의 중간 테이블 #################
        TypeCategoryProduct.objects.create(
            type_category = TypeCategory.objects.get(id=1),
            product       = Product.objects.get(id=1)
        )
        
        TypeCategoryProduct.objects.create(
            type_category = TypeCategory.objects.get(id=1),
            product       = Product.objects.get(id=2)
        )
        
        TypeCategoryProduct.objects.create(
            type_category = TypeCategory.objects.get(id=1),
            product       = Product.objects.get(id=3)
        )

        ################# Image #################
        Image.objects.create(
            id          = 1,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/24/20200824_final_Perfect-Renew-Youth-Regenerating-Cream_thumbnail_01_pc.png",
            product  = Product.objects.get(id = 1)
        )

        Image.objects.create(
            id          = 2,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/24/20200824_final_Perfect-Renew-Youth-Regenerating-Cream_thumbnail_01_pc.png",
            product  = Product.objects.get(id = 1)
        )

        Image.objects.create(
            id          = 3,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/24/20200824_final_Perfect-Renew-Youth-Regenerating-Cream_thumbnail_02_pc.png",
            product  = Product.objects.get(id = 1)
        )

        Image.objects.create(
            id          = 4,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/24/20200824_final_Perfect-Renew-Youth-Regenerating-Cream_thumbnail_01_pc_1.png",
            product  = Product.objects.get(id = 1)
        )

        Image.objects.create(
            id          = 5,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/11/20200811_final_Perfect-Renew-Youth-Skin-Refiner_thumbnail-03_pc.png",
            product  = Product.objects.get(id = 1)
        )

        Image.objects.create(
            id          = 6,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/11/20200811_final_Perfect-Renew-Youth-Skin-Refiner_thumbnail-04_pc.png",
            product  = Product.objects.get(id = 1)
        )

        Image.objects.create(
            id          = 7,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/26/20200826_final_Perfect-Renew-Youth-Regenerator_thumbnail_pc_4.png",
            product  = Product.objects.get(id = 1)
        )

        Image.objects.create(
            id          = 8,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/01/30/radian-c-cream-07.png",
            
            product     = Product.objects.get(id = 2)
        )


        Image.objects.create(
            id          = 9,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/02/07/radian-c-cream-08.png",
            product     = Product.objects.get(id = 2)
        )

        Image.objects.create(
            id          = 10,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/07/03/20200703_final_radian-c-cream_thumbnail.png",
            product     = Product.objects.get(id = 2)
        )
        
        Image.objects.create(
            id          = 11,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/06/16/radian-c-cream-02.png",
            product     = Product.objects.get(id = 2)
        )

        Image.objects.create(
            id          = 12,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/06/16/radian-c-cream-03.png",
            product     = Product.objects.get(id = 2)
        )

        Image.objects.create(
            id          = 13,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/06/16/radian-c-cream-04.png",
            product     = Product.objects.get(id = 2)
        )

        Image.objects.create(
            id          = 14,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/06/16/radian-c-cream-06.png",
            product     = Product.objects.get(id = 2)
        )

        Image.objects.create(
            id          = 15,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/06/16/radian-c-cream-07.png",
            product     = Product.objects.get(id = 2)
        )
        
        Image.objects.create(
            id          = 16,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2019/11/15/Water_Bank_Hydro_Cream_EX_thumb_04_1.png",
            product     = Product.objects.get(id = 3)
        )

        Image.objects.create(
            id          = 17,
            image_url   =      "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2019/11/15/Water_Bank_Hydro_Cream_EX_thumb_list.png",
            product     = Product.objects.get(id = 3)
        )

        Image.objects.create(
            id          = 18,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2019/11/14/Water_Bank_Hydro_Cream_EX_thumb_01_1.png",
            product     = Product.objects.get(id = 3)
        )

        Image.objects.create(
            id          = 19,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2019/12/06/Water_Bank_Hydro_Cream_EX_thumb_02.jpg",
            product     = Product.objects.get(id = 3)
        )

        Image.objects.create(
            id          = 20,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2019/11/15/Water_Bank_Hydro_Cream_EX_thumb_03.png",
            product     = Product.objects.get(id = 3)
        )

        Image.objects.create(
            id          = 21,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2019/12/06/Water_Bank_Hydro_Cream_EX_thumb_04.jpg",
            product     = Product.objects.get(id = 3)
        )

        Image.objects.create(
            id          = 22,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2019/12/06/Water_Bank_Hydro_Cream_EX_thumb_05.png",
            product     = Product.objects.get(id = 3)
        )

        ################# HtmlTag #################
        HtmlTag.objects.create(
            id      = 1,
            detail  = "Product no.1 detail HTML..",
            product = Product.objects.get(id = 1)
        )
        HtmlTag.objects.create(
            id      = 2,
            detail  = "Product no.2 detail HTML..",
            product = Product.objects.get(id = 2)
        )
        HtmlTag.objects.create(
            id      = 3,
            detail  = "Product no.3 detail HTML..",
            product = Product.objects.get(id = 3)
        )

        ################# Description #################
        Description.objects.create(
            id          = 1,
            description = "유화 과정이 별도로 필요 없는 밀크 오일 제형으로 메이크업과 각질을 부드럽게 멜팅해주는 약산성 클렌저에요.",
            product     = Product.objects.get(id = 1)
        )
        Description.objects.create(
            id          = 2,
            description = "눈에 보이지 않는 초미세잡티까지 제거하는 강력한 Radian-C Super BlendTM가 함유된 저자극 고보습 비타민 크림이에요.",
            product     = Product.objects.get(id = 2)            
        )
        Description.objects.create(
            id          = 3,
            description = "그린 미네랄 워터로 피부에 깊은 수분감을 채워 24시간 촉촉하고 산뜻한 수분막을 선사하는 고수분 크림이에요.",
            product     = Product.objects.get(id = 3)            
        )

        ################# Precaution #################
        Precaution.objects.create(
            id         = 1,
            precaution = "진성분 1",
            product    = Product.objects.get(id = 1)
        )
        Precaution.objects.create(
            id         = 2,
            precaution = "진성분 2",
            product    = Product.objects.get(id = 2)
        )
        Precaution.objects.create(
            id         = 3,
            precaution = "진성분 3",
            product    = Product.objects.get(id = 3)
        )
        
        ################# Size #################

        Size.objects.create(
            id       = 1,
            size     = "150ml",
            product  = Product.objects.get(id = 1)
        )

        Size.objects.create(
            id       = 2,
            size     = "100ml",
            product  = Product.objects.get(id = 2)
        )

        Size.objects.create(
            id       = 3,
            size     = "50ml",
            product  = Product.objects.get(id = 3)
        )

        ################# Ingredient #################

        Ingredient.objects.create(
            id         = 1,
            ingredient = "기침,재채기,열,설사1",
            product    = Product.objects.get(id = 1)
        )

        Ingredient.objects.create(
            id         = 2,
            ingredient = "기침,재채기,열,설사2",
            product    = Product.objects.get(id = 2)
        )

        Ingredient.objects.create(
            id         = 3,
            ingredient = "기침,재채기,열,설사3",
            product    = Product.objects.get(id = 3)
        )

        ################# Tag #################

        Tag.objects.create(
            id       = 1,
            tag      = "산뜻1",
            product  = Product.objects.get(id = 1)
        )

        Tag.objects.create(
            id       = 2,
            tag      = "촉촉1",
            product  = Product.objects.get(id = 1)
        )

        Tag.objects.create(
            id       = 3,
            tag      = "산뜻2",
            product  = Product.objects.get(id = 2)
        )

        Tag.objects.create(
            id       = 4,
            tag      = "촉촉2",
            product  = Product.objects.get(id = 2)
        )
        
        Tag.objects.create(
            id       = 5,
            tag      = "산뜻3",
            product  = Product.objects.get(id = 3)
        )

        Tag.objects.create(
            id       = 6,
            tag      =  "촉촉3",
            product  = Product.objects.get(id = 3)
        )

    def tearDown(self):
        MainCategory.objects.all().delete()
        SubCategory.objects.all().delete()
        TypeCategory.objects.all().delete()
        Product.objects.all().delete()
        TypeCategoryProduct.objects.all().delete()
        Image.objects.all().delete()
        HtmlTag.objects.all().delete()
        Description.objects.all().delete
        Precaution.objects.all().delete
        Size.objects.all().delete
        Ingredient.objects.all().delete
        Tag.objects.all().delete

    def test_productlist_get_success(self):
        client   = Client()
        response = client.get('/product/list?type=1', content_type = 'application/json')
        result = {
            "tot_page" : 1,
            "data": [
                {
                    "main_category": "스킨케어",
                    "sub_category" : "유형별",
                    "type_category": "젤/크림",
                    "id"           : 1,
                    "korean_name"  : "퍼펙트 리뷰 유스 리제너레이팅 크림",
                    "image"        : [
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/24/20200824_final_Perfect-Renew-Youth-Regenerating-Cream_thumbnail_01_pc.png",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/24/20200824_final_Perfect-Renew-Youth-Regenerating-Cream_thumbnail_01_pc.png",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/24/20200824_final_Perfect-Renew-Youth-Regenerating-Cream_thumbnail_02_pc.png",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/24/20200824_final_Perfect-Renew-Youth-Regenerating-Cream_thumbnail_01_pc_1.png",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/11/20200811_final_Perfect-Renew-Youth-Skin-Refiner_thumbnail-03_pc.png",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/11/20200811_final_Perfect-Renew-Youth-Skin-Refiner_thumbnail-04_pc.png",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/26/20200826_final_Perfect-Renew-Youth-Regenerator_thumbnail_pc_4.png"
                                    ],
                    "tag"          : ["산뜻1","촉촉1"]
                },
                {
                    "main_category": "스킨케어",
                    "sub_category" : "유형별",
                    "type_category": "젤/크림",
                    "id"           : 2,
                    "korean_name"  : "래디언-C 크림",
                    "image"        : [
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/01/30/radian-c-cream-07.png",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/02/07/radian-c-cream-08.png",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/07/03/20200703_final_radian-c-cream_thumbnail.png",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/06/16/radian-c-cream-02.png",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/06/16/radian-c-cream-03.png",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/06/16/radian-c-cream-04.png",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/06/16/radian-c-cream-06.png",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/06/16/radian-c-cream-07.png"
                                    ],
                    "tag"          : ["산뜻2", "촉촉2"]
                },
                {
                    "main_category": "스킨케어",
                    "sub_category" : "유형별",
                    "type_category": "젤/크림",
                    "id"           : 3,
                    "korean_name"  : "워터뱅크 하이드로 크림 EX",
                    "image"        : [
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2019/11/15/Water_Bank_Hydro_Cream_EX_thumb_04_1.png",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2019/11/15/Water_Bank_Hydro_Cream_EX_thumb_list.png",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2019/11/14/Water_Bank_Hydro_Cream_EX_thumb_01_1.png",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2019/12/06/Water_Bank_Hydro_Cream_EX_thumb_02.jpg",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2019/11/15/Water_Bank_Hydro_Cream_EX_thumb_03.png",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2019/12/06/Water_Bank_Hydro_Cream_EX_thumb_04.jpg",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2019/12/06/Water_Bank_Hydro_Cream_EX_thumb_05.png"
                                    ],
                    "tag"          : ["산뜻3", "촉촉3"]
                }
            ]
        }

        self.assertEqual(response.json(), result)
        self.assertEqual(response.status_code, 200)


    def test_productlist_get_not_found(self):
        client = Client()
        response = client.get('/product?menu_id=8', content_type = 'application/json')

        self.assertEqual(response.status_code, 404)    

    # def test_productlist_keyerror(self):
    #     client   = Client()
    #     response = client.get('/product/list?sub=asd', content_type = 'application/json')

    #     self.assertEqual(response.status_code, 400)

class ProductDetailTest(TestCase):

    maxDiff = None

    def setUp(self):
        client = Client()

        ################# MainCategory #################
        MainCategory.objects.create(
            id   = 1,
            name = "스킨케어"
        )

        ################# SubCategory #################
        SubCategory.objects.create(
            id   =  1,
            name =  "유형별",
            main_category = MainCategory.objects.get(id=1)
        )

        ################# TypeCategory #################
        TypeCategory.objects.create(
            id = 1,
            name = "젤/크림",
            sub_category = SubCategory.objects.get(id=1)
        )

        ################# Product #################
        Product.objects.create(
            id           = 1,
            korean_name  = "퍼펙트 리뷰 유스 리제너레이팅 크림",
            english_name = "PERFECT RENEW YOUTH REGENERATING CREAM",
            price        = 65000
        )

        ################# Product 와 TypeCategory의 중간 테이블 #################
        TypeCategoryProduct.objects.create(
            type_category = TypeCategory.objects.get(id=1),
            product       = Product.objects.get(id=1)
        )

        ################# Image #################
        Image.objects.create(
            id          = 1,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/24/20200824_final_Perfect-Renew-Youth-Regenerating-Cream_thumbnail_01_pc.png",
            product  = Product.objects.get(id = 1)
        )

        Image.objects.create(
            id          = 2,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/24/20200824_final_Perfect-Renew-Youth-Regenerating-Cream_thumbnail_01_pc.png",
            product  = Product.objects.get(id = 1)
        )

        Image.objects.create(
            id          = 3,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/24/20200824_final_Perfect-Renew-Youth-Regenerating-Cream_thumbnail_02_pc.png",
            product  = Product.objects.get(id = 1)
        )

        Image.objects.create(
            id          = 4,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/24/20200824_final_Perfect-Renew-Youth-Regenerating-Cream_thumbnail_01_pc_1.png",
            product  = Product.objects.get(id = 1)
        )

        Image.objects.create(
            id          = 5,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/11/20200811_final_Perfect-Renew-Youth-Skin-Refiner_thumbnail-03_pc.png",
            product  = Product.objects.get(id = 1)
        )

        Image.objects.create(
            id          = 6,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/11/20200811_final_Perfect-Renew-Youth-Skin-Refiner_thumbnail-04_pc.png",
            product  = Product.objects.get(id = 1)
        )

        Image.objects.create(
            id          = 7,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/26/20200826_final_Perfect-Renew-Youth-Regenerator_thumbnail_pc_4.png",
            product  = Product.objects.get(id = 1)
        )

        ################# HtmlTag #################
        HtmlTag.objects.create(
            id      = 1,
            detail  = "Product no.1 detail HTML..",
            product = Product.objects.get(id = 1)
        )

        ################# Description #################
        Description.objects.create(
            id          = 1,
            description = "유화 과정이 별도로 필요 없는 밀크 오일 제형으로 메이크업과 각질을 부드럽게 멜팅해주는 약산성 클렌저에요.",
            product     = Product.objects.get(id = 1)
        )

        ################# Precaution #################
        Precaution.objects.create(
            id         = 1,
            precaution = "진성분 1",
            product    = Product.objects.get(id = 1)
        )
        
        ################# Size #################

        Size.objects.create(
            id       = 1,
            size     = "150ml",
            product  = Product.objects.get(id = 1)
        )

        ################# Ingredient #################

        Ingredient.objects.create(
            id         = 1,
            ingredient = "기침,재채기,열,설사1",
            product    = Product.objects.get(id = 1)
        )
        ################# Tag #################

        Tag.objects.create(
            id       = 1,
            tag      = "산뜻1",
            product  = Product.objects.get(id = 1)
        )

        Tag.objects.create(
            id       = 2,
            tag      = "촉촉1",
            product  = Product.objects.get(id = 1)
        )
            
    def tearDown(self):
        MainCategory.objects.all().delete()
        SubCategory.objects.all().delete()
        TypeCategory.objects.all().delete()
        Product.objects.all().delete()
        TypeCategoryProduct.objects.all().delete()
        Image.objects.all().delete()
        HtmlTag.objects.all().delete()
        Description.objects.all().delete
        Precaution.objects.all().delete
        Size.objects.all().delete
        Ingredient.objects.all().delete
        Tag.objects.all().delete

    def test_productdetail_get_success(self):
        client   = Client()
        response = client.get('/product/list/1?type=1', content_type = 'application/json')
        result = {
            "data": [
                {
                    "product_id"   : 1,
                    "main_category": "스킨케어",
                    "sub_category" : "유형별",
                    "type_category": "젤/크림",
                    "korean_name"  : "퍼펙트 리뷰 유스 리제너레이팅 크림",
                    "english_name" : "PERFECT RENEW YOUTH REGENERATING CREAM",
                    "size"         : "150ml",
                    "price"        : 65000,
                    "image"        : [
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/24/20200824_final_Perfect-Renew-Youth-Regenerating-Cream_thumbnail_01_pc.png",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/24/20200824_final_Perfect-Renew-Youth-Regenerating-Cream_thumbnail_01_pc.png",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/24/20200824_final_Perfect-Renew-Youth-Regenerating-Cream_thumbnail_02_pc.png",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/24/20200824_final_Perfect-Renew-Youth-Regenerating-Cream_thumbnail_01_pc_1.png",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/11/20200811_final_Perfect-Renew-Youth-Skin-Refiner_thumbnail-03_pc.png",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/11/20200811_final_Perfect-Renew-Youth-Skin-Refiner_thumbnail-04_pc.png",
                                    "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/26/20200826_final_Perfect-Renew-Youth-Regenerator_thumbnail_pc_4.png"
                                    ],
                    "tag"          : ["산뜻1", "촉촉1"],
                    "detail"       : "Product no.1 detail HTML..",
                    "precaution"   : "진성분 1",
                    "ingredient"   : "기침,재채기,열,설사1",
                    "description"  : "유화 과정이 별도로 필요 없는 밀크 오일 제형으로 메이크업과 각질을 부드럽게 멜팅해주는 약산성 클렌저에요.",
                }
            ]
        }
        
        self.assertEqual(response.json(), result)
        self.assertEqual(response.status_code, 200)

    def test_productlist_get_not_found(self):
        client = Client()
        response = client.get('/product/1', content_type = 'application/json')

        self.assertEqual(response.status_code, 404)  


class ProductTypeListView(TestCase):

    maxDiff = None

    def setUp(self):
        client = Client()

        MainCategory.objects.create(
            id = 1,
            name = "스킨케어"
        )

        SubCategory.objects.create(
            id = 1,
            name = "유형별",
            main_category = MainCategory.objects.get(id=1)
        )

        TypeCategory.objects.create(
            id = 1,
            name = "젤/크림",
            sub_category = SubCategory.objects.get(id=1)
        )

        TypeCategory.objects.create(
            id = 2,
            name = "스킨/미스트",
            sub_category = SubCategory.objects.get(id=1)
        )

        TypeCategory.objects.create(
            id = 3,
            name = "마스크팩",
            sub_category = SubCategory.objects.get(id=1)
        )

    def tearDown(self):
        MainCategory.objects.all().delete()
        SubCategory.objects.all().delete()
        TypeCategory.objects.all().delete()
        
    def test_typelist_get_success(self):
        client = Client()
        response = client.get('/product/type/list', content_type = 'application/json')
        result = {
            "data": [
                {
                "main_category"     : "스킨케어",
                "sub_category_id"   : 1,
                "sub_category"      : "유형별",
                "type_category_id"  : 1,
                "type_category"     : "젤/크림"   
                 },
                {
                "main_category"     : "스킨케어",
                "sub_category_id"   : 1,
                "sub_category"      : "유형별",
                "type_category_id"  : 2,
                "type_category"     : "스킨/미스트"   
                 },
                {
                "main_category"     : "스킨케어",
                "sub_category_id"   : 1,
                "sub_category"      : "유형별",
                "type_category_id"  : 3,
                "type_category"     : "마스크팩"   
                 }
            ]
        }
        
        self.assertEqual(response.json(), result)
        self.assertEqual(response.status_code, 200)
    
    def test_productdetail_get_not_found(self):
        client = Client()
        response = client.get('/type/list', content_type = 'text/html')
        
        self.assertEqual(response.status_code, 404)
        
class ProductSearchView(TestCase):

    maxDiff = None

    def setUp(self):
        client = Client()

        Product.objects.create(
            id           = 1,
            korean_name  = "퍼펙트 리뷰 유스 리제너레이팅 크림",
            english_name = "PERFECT RENEW YOUTH REGENERATING CREAM",
            price        = 65000                        
        )

        Product.objects.create(
            id           = 2,
            korean_name  = "래디언-C 크림",
            english_name = "RADIAN-C CREAM",
            price        = 29000
        )

        Image.objects.create(
            id          = 1,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/24/20200824_final_Perfect-Renew-Youth-Regenerating-Cream_thumbnail_01_pc.png",
            product  = Product.objects.get(id = 1)
        )

        Image.objects.create(
            id          = 2,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/24/20200824_final_Perfect-Renew-Youth-Regenerating-Cream_thumbnail_01_pc.png",
            product  = Product.objects.get(id = 1)
        )

        Image.objects.create(
            id          = 3,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/24/20200824_final_Perfect-Renew-Youth-Regenerating-Cream_thumbnail_02_pc.png",
            product  = Product.objects.get(id = 1)
        )

        Image.objects.create(
            id          = 4,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/24/20200824_final_Perfect-Renew-Youth-Regenerating-Cream_thumbnail_01_pc_1.png",
            product  = Product.objects.get(id = 1)
        )

        Image.objects.create(
            id          = 5,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/11/20200811_final_Perfect-Renew-Youth-Skin-Refiner_thumbnail-03_pc.png",
            product  = Product.objects.get(id = 1)
        )

        Image.objects.create(
            id          = 6,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/11/20200811_final_Perfect-Renew-Youth-Skin-Refiner_thumbnail-04_pc.png",
            product  = Product.objects.get(id = 1)
        )

        Image.objects.create(
            id          = 7,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/26/20200826_final_Perfect-Renew-Youth-Regenerator_thumbnail_pc_4.png",
            product  = Product.objects.get(id = 1)
        )

        Image.objects.create(
            id          = 8,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/01/30/radian-c-cream-07.png",
            
            product     = Product.objects.get(id = 2)
        )


        Image.objects.create(
            id          = 9,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/02/07/radian-c-cream-08.png",
            product     = Product.objects.get(id = 2)
        )

        Image.objects.create(
            id          = 10,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/07/03/20200703_final_radian-c-cream_thumbnail.png",
            product     = Product.objects.get(id = 2)
        )
        
        Image.objects.create(
            id          = 11,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/06/16/radian-c-cream-02.png",
            product     = Product.objects.get(id = 2)
        )

        Image.objects.create(
            id          = 12,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/06/16/radian-c-cream-03.png",
            product     = Product.objects.get(id = 2)
        )

        Image.objects.create(
            id          = 13,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/06/16/radian-c-cream-04.png",
            product     = Product.objects.get(id = 2)
        )

        Image.objects.create(
            id          = 14,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/06/16/radian-c-cream-06.png",
            product     = Product.objects.get(id = 2)
        )

        Image.objects.create(
            id          = 15,
            image_url   = "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/06/16/radian-c-cream-07.png",
            product     = Product.objects.get(id = 2)
        )

        Tag.objects.create(
            id       = 1,
            tag      = "산뜻1",
            product  = Product.objects.get(id = 1)
        )

        Tag.objects.create(
            id       = 2,
            tag      = "촉촉1",
            product  = Product.objects.get(id = 1)
        )

        Tag.objects.create(
            id       = 3,
            tag      = "산뜻2",
            product  = Product.objects.get(id = 2)
        )

        Tag.objects.create(
            id       = 4,
            tag      = "촉촉2",
            product  = Product.objects.get(id = 2)
        )

    def tearDown(self):
        Product.objects.all().delete()
        Image.objects.all().delete()
        Tag.objects.all().delete()

    def test_productsearch_get_success(self):
        client = Client()
        response = client.get('/product/search?keyword=크림', content_type = 'application/json')
        result = {
            'data':[
                {
                "id"           : 1,
                "korean_name"  : '퍼펙트 리뷰 유스 리제너레이팅 크림',
                "image"        : ["https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/24/20200824_final_Perfect-Renew-Youth-Regenerating-Cream_thumbnail_01_pc.png",
                "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/24/20200824_final_Perfect-Renew-Youth-Regenerating-Cream_thumbnail_01_pc.png",
                "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/24/20200824_final_Perfect-Renew-Youth-Regenerating-Cream_thumbnail_02_pc.png",
                "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/24/20200824_final_Perfect-Renew-Youth-Regenerating-Cream_thumbnail_01_pc_1.png",
                "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/11/20200811_final_Perfect-Renew-Youth-Skin-Refiner_thumbnail-03_pc.png",
                "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/11/20200811_final_Perfect-Renew-Youth-Skin-Refiner_thumbnail-04_pc.png",
                "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/08/26/20200826_final_Perfect-Renew-Youth-Regenerator_thumbnail_pc_4.png"
                ],
                "tag"          : ["산뜻1","촉촉1"]
                },
                {
                "id"           : 2,
                "korean_name"  : "래디언-C 크림",
                "image"        : ["https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/01/30/radian-c-cream-07.png",
                "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/02/07/radian-c-cream-08.png",
                "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/07/03/20200703_final_radian-c-cream_thumbnail.png",
                "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/06/16/radian-c-cream-02.png",
                "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/06/16/radian-c-cream-03.png",
                "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/06/16/radian-c-cream-04.png",
                "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/06/16/radian-c-cream-06.png",
                "https://www.laneige.com/kr/ko/skincare/__icsFiles/afieldfile/2020/06/16/radian-c-cream-07.png"
                ],
                "tag"          : ["산뜻2", "촉촉2"]
                } 
            ]
        }

        self.assertEqual(response.json(), result)
        self.assertEqual(response.status_code, 200)

    def test_productsearch_get_not_found(self):
        client   = Client()
        response = client.get('product/search?product_id=1', content_type = 'application/json')

        self.assertEqual(response.status_code, 404)
