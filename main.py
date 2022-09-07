from config import app
from views import users_blueprint
from utils import init_db

app.register_blueprint(users_blueprint)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)