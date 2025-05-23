from flask import Blueprint,request,jsonify
from app.models.customer_model import Customer
from app.extensions import db
from app.status_codes import HTTP_400_BAD_REQUEST,HTTP_201_CREATED,HTTP_500_INTERNAL_SERVER_ERROR

#registering the blueprint
customer = Blueprint('customer',__name__,url_prefix="/api/v1/customer")

#creating a customer
@customer.route("/create",methods=['POST'])
def create_customer():

    #storing request values
    data = request.json
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email = data.get("email")
    contact = data.get("contact")
    

    #validating request
    if not first_name or not last_name or not email or not contact:
        return jsonify({
            "Error":"ALL fields is requred"
        }),HTTP_400_BAD_REQUEST
    
    try:
        #creating a new customer
        new_customer = Customer(first_name=first_name,last_name=last_name,email=email,contact=contact)
        db.session.add(new_customer)
        db.session.commit()

        return jsonify({
            "Message":"customer created successfully",
            "customer":{
                "id":new_customer.id,
                "first_name":new_customer.first_name,
                "last_name":new_customer.last_name,
                "email":new_customer.email,
                "contact":new_customer.contact
                }
            }),HTTP_201_CREATED
    except Exception as e:
        return  jsonify({
            "Error":str(e)
        }),HTTP_500_INTERNAL_SERVER_ERROR