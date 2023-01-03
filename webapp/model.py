from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # первичный ключ
    title = db.Column(db.String, nullable=False)  # nullable - данные должны быть обязательно
    url = db.Column(db.String, unique=True, nullable=False)  # unique уникальный адрес должен быть
    published = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=True) # nullable - данные могут не содержаться

    def __repr__(self):  # магический метод
        return '<News {} {}>'.format(self.title, self.url)