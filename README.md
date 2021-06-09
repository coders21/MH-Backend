# MobileHutStore
An online retail site through which user can do online shopping

## Prequistes

* Python 3
* Django
* Django Rest Framework
* Node JS
* React JS
* NPM

## Installing Guide

* Clone Repo
* Create virtual environment
* Activate virtual  environment
* Run pip3 install -r requirements.txt
* Run python manage.py makemigrations
* Run python manage.py migrate
* Run python manage.py runserver

## Testing

### Login:
* create superuser, using python manage.py createsuperuser and tests it with below api it should return access token
* http://127.0.0.1:8000/AuthApp/jwt/
* you will get data in this format:
    {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluQGdtYWlsLmNvbSIsImV4cCI6MTYwOTkyMzk1NCwiZW1haWwiOiJhZG1pbkBnbWFpbC5jb20ifQ.ekHXYkxk7TCMVRx3_Ap2_FZeWLJb2756Un2_Qgz4Qjo",
    "user": {
        "username": "admin@gmail.com",
        "id": 1
    }
}

### Category Endpoint:
* http://127.0.0.1:8000/Products/create_category/ (Create)
* Endpoint Data to create Category:
    {
    "category_name": "Headphones"
    }
* http://127.0.0.1:8000/Products/manage_categories/id (Edit,Delete)
* Endpoint Data to edit Category:
    {
    "id":1
    "category_name": "Powerbanks"
    }
* Endpoint Data to delete category:
    {
    "id": 1,
    }
    
### Brand EndPoint:
* http://127.0.0.1:8000/Products/create_brand/ (Create)
* Endpoint Data to create Category:
    {
    "brand_name": "baseus"
    }
* http://127.0.0.1:8000/Products/manage_brand/id (Edit,Delete)
* Endpoint Data to edit brand:
    {
    "id":1
    "brand_name": "romoss"
    }
* Endpoint Data to delete brand:
    {
    "id": 1,
    }
    
### ModelType (Product Models):
* http://127.0.0.1:8000/Products/create_model/ (Create)
* Endpoint Data to create Model:
    {
    "model_name": "ipad air 2"
    }
* http://127.0.0.1:8000/Products/manage_model/id (Edit,Delete)
* Endpoint Data to edit model:
    {
    "id":1
    "model_name": "ipad pro 10.5"
    }
* Endpoint Data to delete model:
    {
    "id": 1,
    }
### Products Endpoint:
* http://127.0.0.1:8000/Products/create_products (Create)
* {
    "product_name":"xyz",
    "product_sku":"abc",
    "product_description":"This is good",
    "product_quantity":100,
    "product_price":200,
    "product_category":1  # (Passing id of category)
    "product_brand":1       # (Passing id of brand)
    "product_model":1     # (Passing id of model)
    }

* http://127.0.0.1:8000/Products/manage_products/id/  (Edit,Delete)
* Endpoint to edit product:
* {
    "id":1,
    "product_name":"xyz",
    "product_sku":"abc",
    "product_description":"This is good",
    "product_quantity":100,
    "product_price":200,
    "product_category":1  # (Passing id of category)
    "product_brand":1       # (Passing id of brand)
    "product_model":1     # (Passing id of model)
    }
 * Endpoint to delete product
 * {
     "id":1
    }
### Colour Endpoint:
* http://127.0.0.1:8000/Products/create_colour/
* Endpoint Data to create Colour:
    {
    "colour_name": "black"
    "colour_product": 1 ( Passing product id)
    }
* http://127.0.0.1:8000/Products/manage_colour/1
* Endpoint Data to edit Colour:
    {
    "id":1
    "colour_name": "green"
    "colour_product": 1 ( Passing product id)
    }
* Endpoint to delete colour:
  {
     "id":1
   }

# Orders
* To get,create all orders <br/>
* http://127.0.0.1:8000/Orders/create_order/ <br/>
* Endpoint format <br />
 { <br />
        "id": 1, <br />
        "order_date": "2021-01-23", <br />
        "order_status": "delivery failed", <br />
        "order_returndate": "2021-01-24" <br />
    }, <br />
 * To edit Orders
 * http://127.0.0.1:8000/Orders/manage_order/id <br/>
 * { <br />
        "id": 1, <br />
        "order_date": "2021-01-23", <br />
        "order_status": "delivery failed", <br />
        "order_returndate": "2021-01-24" <br />
    }, <br />

# Product Orders
* To create and get all product orders <br/>
* http://127.0.0.1:8000/Orders/create_porder/ <br />
* Endpoint <br/>
* 
    {
        "id": 1, <br/>
        "quantity": 24, <br/>
        "product": 1, <br/>
        "user": 1, <br />
        "order": 1 <br />
    }, <br/>
* to edit http://127.0.0.1:8000/Orders/manage_porder/1 <br />

# Get All brand,model,order,product
* http://127.0.0.1:8000/Products/get_total/ <br/>

* Endpoint <br/>
{ <br/>
    "total_brands": 1,<br/>
    "total_models": 1,<br/>
    "total_categories": 1,<br/>
    "total_products": 1,<br/>
    "total_orders": 2<br/>
}
