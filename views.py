from flask import jsonify, Blueprint, request, json

import models
from flask import current_app as app

from config import db

users_blueprint = Blueprint('users_blueprint', __name__)



@users_blueprint.route("/users", methods=['GET', 'POST'])
def users_page():
    if request.method == 'GET':
        result = []
        for user in models.User.query.all():
            result.append(user.users_to_dict())
        return jsonify(result), 200
    elif request.method == 'POST':
        users_list = json.loads(request.data)
        new_user = models.User(**users_list)
        db.session.add(new_user)
        db.session.commit()
        result = []
        for user in models.User.query.all():
            result.append(user.users_to_dict())
        return result

@users_blueprint.route("/users/<int:id>", methods=['GET', 'POST', 'DELETE'])
def one_user_page(id):
    if request.method == 'GET':
        user = models.User.query.get(id)
        return jsonify(user.users_to_dict())
    if request.method == 'PUT':
        user_data = request.json()
        user = models.User.query.get(id)
        user.first_name = user_data['first_name']
        user.last_name = user_data['last_name']
        user.age = user_data['age']
        user.email = user_data['email']
        user.role = user_data['role']
        user.phone = user_data['phone']

        db.session.add(user)
        db.session.commit()

        user = models.User.query.get(id)
        return user
    if request.method == 'DELETE':
        user = models.User.query.get(id)
        db.session.delete(user)
        db.session.commit()

        return "", 200


@users_blueprint.route("/orders", methods=['GET', 'POST'])
def orders_page():
    if request.method == 'GET':
        result = []
        for order in models.Order.query.all():
            result.append(order.order_to_dict())
        return jsonify(result), {'Content-type': 'application/json; charset=utf-8'}
    elif request.method == 'POST':
        order_list = json.loads(request.data)
        new_order = models.User(**order_list)
        db.session.add(new_order)
        db.session.commit()

        result = []
        for order in models.Order.query.all():
            result.append(order.order_to_dict())
        return result


@users_blueprint.route("/orders/<int:id>", methods=['GET', 'POST', 'DELETE'])
def one_order_page(id):
    if request.method == 'GET':
        order = models.Order.query.get(id)
        return jsonify(order.order_to_dict())
    if request.method == 'PUT':
        order_data = request.json()
        order = models.Order.query.get(id)
        order.name = order_data['name']
        order.description = order_data['description']
        order.start_date = order_data['start_date']
        order.end_date = order_data['end_date']
        order.address = order_data['address']
        order.price = order_data['price']

        db.session.add(order)
        db.session.commit()

        user = models.Order.query.get(id)
        return user
    if request.method == 'DELETE':
        order = models.Order.query.get(id)
        db.session.delete(order)
        db.session.commit()

        return "", 200


@users_blueprint.route("/offers", methods=['GET', 'POST'])
def offers_page():
    if request.method == 'GET':
        result = []
        for offer in models.Offer.query.all():
            result.append(offer.offer_to_dict())
        return jsonify(result), 200
    elif request.method == 'POST':
        offer_list = json.loads(request.data)
        new_offer = models.User(**offer_list)
        db.session.add(new_offer)
        db.session.commit()

        result = []
        for offer in models.Offer.query.all():
            result.append(offer.offer_to_dict())
        return result


@users_blueprint.route("/offers/<int:id>", methods=['GET', 'POST', 'DELETE'])
def one_offer(id):
    if request.method == 'GET':
        offer = models.Offer.query.get(id)
        return jsonify(offer.offer_to_dict())
    if request.method == 'PUT':
        offer_data = request.json()
        offer = models.Offer.query.get(id)
        offer.order_id = offer_data['order_id']
        offer.executor_id = offer_data['executor_id']

        db.session.add(offer)
        db.session.commit()

        offer = models.Offer.query.get(id)
        return offer
    if request.method == 'DELETE':
        offer = models.Offer.query.get(id)
        db.session.delete(offer)
        db.session.commit()

        return "", 200