from .models import Category,Brand,Product,ProductImages,ModelType,ProductModel,Colour
from Orders.models import ProductOrder
from Homepage.models import Sale,ProductSale,RecommendedProduct
import random
from datetime import datetime,date,timedelta

def getcategoryProducts(id):
   
    prod=Product.objects.filter(product_category=id).select_related('product_category','product_brand')
    product_data=productformat(prod)
    
    return product_data
    

def getbrandProducts(id):

    prod=Product.objects.filter(product_brand=id).select_related('product_category','product_brand')
    product_data=productformat(prod)
    
    return product_data

def getunder99Products():

    prod=Product.objects.filter(sale_price__lte=99).select_related('product_category','product_brand')
    product_data=productformat(prod)

    return product_data

def getclearanceProducts():

    prod=Product.objects.all().order_by('id')[:40].select_related('product_category','product_brand')
    product_data=productformat(prod)

    return product_data


def gettrendingProducts():

     prod=Product.objects.all().order_by('review_count')
     product_data=productformat(prod)
     return product_data


def getrecommendedProducts():
    prod=RecommendedProduct.objects.all().select_related('product')
    product_data=productformatSecond(prod)

    return product_data
    
def getbuyerpickProducts():

    prod= Product.objects.filter(productorder__isnull=False).select_related('product_category','product_brand').distinct()

    if len(prod)<1:
        prod=Product.objects.all()[:10]

    product_data=productformat(prod)


    return product_data

def getnewarrivalProducts():
    
    prod=Product.objects.all().prefetch_related('productimages_set').select_related('product_category','product_brand')
    d_prod=[]
    for prod in prod:
        mydate=prod.created_date
        mydate_limit = mydate + timedelta(days=+14)
        if date.today() < mydate_limit:
            d_prod.append(prod)

    new_arrival_product=productformat(d_prod)
    
    return new_arrival_product

def getsaleProducts():
     
     sale=None
     product_data=None

     try:
            sale=Sale.objects.get(startdate__lte=datetime.today().strftime('%Y-%m-%d'),enddate__gte=datetime.today().strftime('%Y-%m-%d'))
     except (KeyError, Sale.DoesNotExist):
            pass
     else:
            prod=ProductSale.objects.filter(sale=sale.id).select_related('product')
            product_data=productformatSecond(prod)

     return product_data


def productformatSecond(prod):

            product_data={}
            sale=None
            save_val=True

            brand_append=[]
            brand={}
            category_append=[]
            category={}
            sale_product=[]

            for prod in prod:
                for x in range (0,len(sale_product)): # check duplicate
                        if prod.product.id==sale_product[x]['product_id']:
                            save_val=False
                            break
                if save_val:
                    images=prod.product.productimages_set.all().order_by('id')[:2].values()
                    sale_product.append({"product_id":prod.product.id,"product_name":prod.product.product_name,"stock":prod.product.product_quantity,"product_price":prod.product.product_price,
                    "sale_price":prod.product.sale_price,"saleprice_startdate":prod.product.saleprice_startdate,
                    "saleprice_enddate":prod.product.saleprice_enddate,"product_category":prod.product.category_name,"product_reviews":prod.product.product_reviews,"review_count":prod.product.review_count,
                    "product_images":images})
                    product_data['product']=sale_product
                save_val=True

                for x in range (0,len(category_append)): # check duplicate category
                        if prod.product.product_category.id==category_append[x]['id']:
                            save_val=False
                            break

                if (save_val):
                    category['name']=prod.product.product_category.category_name
                    category['id']=prod.product.product_category.id
                    category_append.append(category)
                    product_data["category"]=category_append
                
                category={}
            
                save_val=True

                # remove duplicate brands
                for x in range (0,len(brand_append)): # check duplicate
                        if prod.product.product_brand.id==brand_append[x]['id']:
                            save_val=False
                            break
                if (save_val):
                    brand['name']=prod.product.product_brand.brand_name
                    brand['id']=prod.product.product_brand.id 
                    brand_append.append(brand)
                    product_data["brand"]=brand_append
                    
                
                brand={}
                save_val=True
            # product_data=productformat(prod)
    
            return product_data



def productformat(prod): # format to show data of products list

    brand_append=[]
    brand={}
    category_append=[]
    category={}
    show_product=[]
    product_data={}
    
    save_val=True

    for prod in prod:
                images=prod.productimages_set.all().order_by('id')[:2].values()
                show_product.append({"product_id":prod.id,"product_name":prod.product_name,"stock":prod.product_quantity,"product_price":prod.product_price,
                "sale_price":prod.sale_price,"created_date":prod.created_date,"saleprice_startdate":prod.saleprice_startdate,
                "saleprice_enddate":prod.saleprice_enddate,"product_brand":prod.product_brand.brand_name,"product_category":prod.category_name,"product_review":prod.product_reviews,"review_count":prod.review_count,
                "product_images":images})

                # remove duplicate categories
                for x in range (0,len(category_append)): # check duplicate
                        if prod.product_category.id==category_append[x]['id']:
                            save_val=False
                            break
                if (save_val):
                    category['name']=prod.product_category.category_name
                    category['id']=prod.product_category.id
                    category_append.append(category)
                    product_data["category"]=category_append
                
                category={}
                brand={}
                save_val=True

                # remove duplicate brands
                for x in range (0,len(brand_append)): # check duplicate
                        if prod.product_brand.id==brand_append[x]['id']:
                            save_val=False
                            break
                if (save_val):
                    brand['name']=prod.product_brand.brand_name
                    brand['id']=prod.product_brand.id 
                    brand_append.append(brand)
                    product_data["brand"]=brand_append
                
                brand={}
                save_val=True
                product_data["product"]=show_product
                

    return product_data
