from .models import Category,Brand,Product,ProductImages,ModelType,ProductModel,Colour

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
                "sale_price":prod.sale_price,"saleprice_startdate":prod.saleprice_startdate,
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
