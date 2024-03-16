from . import db

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    title = db.Column(db.String(80))
    numBedrooms = db.Column(db.String(80))
    numBathrooms = db.Column(db.String(80))
    location = db.Column(db.String(128))
    price = db.Column(db.String(80))
    propertyType = db.Column(db.String(20))
    description = db.Column(db.String(1000))
    photo = db.Column(db.String(128))

    def __init__(self, title, numBedrooms, numBathrooms, location, price, propertyType, description, photo):
        self.title = title
        self.numBedrooms = numBedrooms
        self.numBathrooms = numBathrooms
        self.location = location
        self.price = price
        self.propertyType = propertyType
        self.description = description
        self.photo = photo

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Property %r>' % (self.title)