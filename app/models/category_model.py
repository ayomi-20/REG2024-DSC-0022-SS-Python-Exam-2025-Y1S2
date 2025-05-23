from app.extensions import db
from datetime import datetime

class Category(db.Model):  #creating a model class
    __tablename__ = "categories" #customizing the table name
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    name = db.Column(db.String(50),nullable = False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,onupdate=datetime.utcnow)

    def __init__(self,name,created_at,updated_at): #invoking the constructor of the super class
        super(Category,self).__init__()
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at