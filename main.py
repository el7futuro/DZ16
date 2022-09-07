from config import app
from utils import *

def init_db():
    db.drop_all()  # удаляем все таблицы
    db.create_all()  # создаем их заново и отправляем данные из файлов
    load_users('data/users.json')
    load_orders('data/orders.json')
    load_offers('data/offers.json')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)