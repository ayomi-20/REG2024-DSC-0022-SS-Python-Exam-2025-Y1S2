from flask import Blueprint,request,jsonify
from app.models.product_model import Product
from app.extensions import db
from app.status_codes import HTTP_400_BAD_REQUEST,HTTP_201_CREATED,HTTP_500_INTERNAL_SERVER_ERROR,HTTP_404_NOT_FOUND,HTTP_200_OK

#registering the blueprint
product = Blueprint('product',__name__,url_prefix="/api/v1/product")

#creating a product
@product.route("/create",methods=['POST'])
def create_product():

    #storing request values
    data = request.json
    name = data.get("name")
    price = data.get("price")
    category_id = data.get("category_id")
    

    #validating request
    if not name or not price or not category_id:
        return jsonify({
            "Error":"ALL fields is requred"
        }),HTTP_400_BAD_REQUEST
    
    try:
        #creating a new product
        new_product = product(name=name,price=price,category_id=category_id)
        db.session.add(new_product)
        db.session.commit()

        return jsonify({
            "Message":"product created successfully",
            "product":{
                "id":new_product.id,
                "name":new_product.name,
                "price":new_product.price,
                "created_at":new_product.created_at,
                "category":{
                    "id":new_product.category.id,
                    "name":new_product.category.name
                }
            }
            }),HTTP_201_CREATED
    except Exception as e:
        return  jsonify({
            "Error":str(e)
        }),HTTP_500_INTERNAL_SERVER_ERROR
    
#editing product by id
@product.route('/edit/<int:id>', methods = ['PUT','PATCH']) #working with the route function
def Updateproductdetails(id):
        
        

        try:

            product = Product.query.filter_by(id=id).first()

            if not product:
                 return jsonify({
                      "Error":"Product not found"
                 }),HTTP_404_NOT_FOUND
            else:
                 name = request.get_json().get("name", product.name)
                 price = request.get_json().get("price", product.price)
                 category_id = request.get_json().get("category_id", product.category_id)


                 product.name = name
                 product.price = price
                 product.category_id = category_id

                 db.session.commit()


                 return jsonify({
                      'message': "product details have been updated successfully",
                      'product' : product.id,
                      'name' : product.name,
                      'pricee' : product.price,
                      'category_id' : product.category_id,
                 }),HTTP_200_OK

        except Exception as e:
            return  jsonify({
                 "Error":str(e)
                 }), HTTP_500_INTERNAL_SERVER_ERROR
        
#getting all products
@product.route("/")
def get_all_products():
     try:
          all_products = Product.query.all()
          product_data = []

          for product in all_products:
               product_info = {
                    'id': product.id,
                    "name": product.name,
                    "price": product.price
               }
               product_data.append(product_info)

          return jsonify({"Message":"All products retrieved successfully",
                            "total_products":len(product_data),
                            "products":product_data}),HTTP_200_OK
     except Exception as e:
        return  jsonify({
            "Error":str(e)
        }), HTTP_500_INTERNAL_SERVER_ERROR
     

#deleting a product by id
@product.route("/delete/<int:id>", methods = ["DELETE"])
def delete_product(id):
    try:
        product = Product.query.filter_by(id=id).first()

        if not product:
            return jsonify({"Error":"Product not found"}),HTTP_404_NOT_FOUND
        else:
            db.session.delete(product)
            db.session.commit()
            return jsonify({
                      'message': "Product deleted successfully",
                 }),HTTP_200_OK
    except Exception as e:
            return  jsonify({
                 "Error":str(e)
                 }), HTTP_500_INTERNAL_SERVER_ERROR