from app.extensions import db
from datetime import datetime

class Product(db.Model): #creating a model class
    __tablename__ = "products" #customizing the tablename
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    category_id = db.Column(db.Integer,db.ForeignKey("categories.id"))
    category = db.relationship("Categories",backref="products")
    name = db.Column(db.String(100),nullable=False)
    price = db.Column(db.String(50),nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,onupdate=datetime.utcnow)

    def __init__(self,category_id,name,price,created_at,updated_at): #invoking the constructor of the super class
        super(Product,self).__init__()
        self.category_id = category_id
        self.name = name
        self.price = price
        self.created_at = created_at
        self.updated_at = updated_at