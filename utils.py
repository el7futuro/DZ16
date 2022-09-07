import json
from models import User, Offer, Order
from config import db
from json import JSONDecodeError


def load_json(filename): #которая загрузит данные из файла

        with open(filename, encoding='utf-8') as file:
            json_list = json.load(file)

        return json_list


def load_users(filename):
    users = load_json(filename)
    db.create_all()
    for user in users:
        new_user = User(**user)
        db.session.add(new_user)

    db.session.commit()


def load_offers(filename):
    offers = load_json(filename)
    db.create_all()
    for offer in offers:
        new_offer = Offer(**offer)
        db.session.add(new_offer)

    db.session.commit()


def load_orders(filename):
    orders = load_json(filename)
    db.create_all()
    for order in orders:
        new_order = Order(**order)
        db.session.add(new_order)

    db.session.commit()


def init_db():
    db.drop_all()  # удаляем все таблицы
    db.create_all()  # создаем их заново и отправляем данные из файлов
    load_users('data/users.json')
    load_orders('data/orders.json')
    load_offers('data/offers.json')

# init_db()
# print(User.query.get(1).users_to_dict())
# print(Offer.query.get(1).offer_to_dict())
# print(Order.query.get(1).order_to_dict())