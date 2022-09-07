from flask import jsonify

import models
from flask import current_app as app

from models import *


@app.route("/", methods=['GET'])
def get_all_users():
    result = []
    users = models.User.query.all()
    for user in users:
        result.append(models.User.users_to_dict(user))
    return jsonify(result)
#
#
# @app.route("/guides/<int:gid>", methods=['GET'])
# def get_one(gid):
#     guide = Guide.query.get(gid)
#     return jsonify(instance_to_dict(guide))
#
#
# @app.route("/guides/<int:gid>/delete")
# def delete_guide(gid):
#     guide = Guide.query.get(gid)
#     db.session.delete(guide)
#     db.session.commit()
#     return jsonify("")
#
#
# @app.route("/guides", methods=['POST'])
# def create_guide():
#     data = request.json
#     guide = Guide(
#         surname=data.get('surname'),
#         full_name=data.get('full_name'),
#         tours_count=data.get('tours_count'),
#         bio=data.get('bio'),
#         is_pro=data.get('is_pro'),
#         company=data.get('company')
#     )
#     db.session.add(guide)
#     db.session.commit()
#     return jsonify(instance_to_dict(guide))
