from myproducts import db

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    type_ = db.Column(db.String(length=30), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    units = db.Column(db.Integer(), nullable=False)
    qtr = db.Column(db.Integer(), nullable=False)

    def to_dict(self):
        return {
            'ID': self.id,
            'Product': self.name,
            'Product_Type': self.type_,
            'Price_Per': self.price,
            'Units_Sold': self.units,
            'Quarter': self.qtr
        }

    def __repr__(self):
        return f'Item {self.name}'