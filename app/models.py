from . import db

class Properties(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    no_bedrooms = db.Column(db.Integer)
    no_bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(80))
    price = db.Column(db.Numeric(10,2))
    property_type = db.Column(db.String(20))
    description = db.Column(db.String(200))
    img = db.Column(db.String(80))

    def __init__(self, title, no_bedrooms, no_bathrooms, location, price, property_type, description, img):
        self.title = title
        self.no_bedrooms = no_bedrooms
        self.no_bathrooms = no_bathrooms
        self.location = location
        self.price = price
        self.property_type = property_type
        self.description = description
        self.img = img

    def __repr__(self):
        return '<Property %r>' % (self.title)