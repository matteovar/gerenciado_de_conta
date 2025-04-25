from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Gastos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date)
    categoria = db.Column(db.String(50))
    valor = db.Column(db.Float)
    descricao = db.Column(db.String(200))
