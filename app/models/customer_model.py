from app.extensions import db
from datetime import datetime

class Customer(db.Model): #creating a model class
    __tablename__ = "customers" #customizing the tablename
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    first_name = db.Column(db.String(50),nullable=False)
    last_name = db.Column(db.String(40),nullable=False)
    email = db.Column(db.String(50),nullable=False)
    contact = db.Column(db.String(30),nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,onupdate=datetime.utcnow)

    def __init__(self,first_name,last_name,email,contact,created_at,updated_at):
        super(Customer,self).__init__() #invoking the constructor of the super class
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.contact = contact
        self.created_at = created_at
        self.updated_at = updated_at
    