from flask import Blueprint,request,jsonify
from app.extensions import db
from app.models.category_model import Category
from app.status_codes import HTTP_201_CREATED,HTTP_400_BAD_REQUEST,HTTP_500_INTERNAL_SERVER_ERROR

#registering the blueprint
category = Blueprint('category',__name__,url_prefix="/api/v1/category")

#creating a category
@category.route("/create",methods=['POST'])
def create_category():

    #storing request values
    data = request.json
    name = data.get("name")

    #validating request
    if not name:
        return jsonify({
            "Error":"Name field is requred"
        }),HTTP_400_BAD_REQUEST
    
    try:
        #creating a new category
        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()

        return jsonify({
            "Message":"Category created successfully"
            }),HTTP_201_CREATED
    except Exception as e:
        return  jsonify({
            "Error":str(e)
        }),HTTP_500_INTERNAL_SERVER_ERROR


