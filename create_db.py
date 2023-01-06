from webapp import db, create_app

db.create_all(app=create_app())
# говорим создать модельки для всего апликейшена

