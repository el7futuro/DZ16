from config import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer())
    email = db.Column(db.String(30))
    role = db.Column(db.String(20))
    phone = db.Column(db.String(20))
    order_id = db.Column(db.Integer(), db.ForeignKey('order.id'))
    offer_id = db.Column(db.Integer(), db.ForeignKey('offer.id'))
    # order = db.relationship("Order", backref="user")
    # offer = db.relationship("Offer", backref="user")

    def users_to_dict(self):
        """
        Serialize implementation
        """
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone,
        }


class Offer(db.Model):
    __tablename__ = 'offer'
    id = db.Column(db.Integer(), primary_key=True)
    order_id = db.Column(db.Integer(), db.ForeignKey('order.id'))
    # orders = db.relationship("Order")
    executor_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    # users = db.relationship("User")

    def offer_to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id,
        }


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(20))
    description = db.Column(db.String(100))
    start_date = db.Column(db.String(10))
    end_date = db.Column(db.String(10))
    address = db.Column(db.String(30))
    price = db.Column(db.Integer())
    customer_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    executor_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    # users = db.relationship("User")
    # offers = db.relationship("Offer")
    customer = db.relationship("User", foreign_keys=[customer_id])
    executor = db.relationship("User", foreign_keys=[executor_id])

    def order_to_dict(self):
        """
        Serialize implementation
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "address": self.address,
            "price": self.price,
            "customer_id": self.customer_id,
            "executor_id": self.executor_id,
        }