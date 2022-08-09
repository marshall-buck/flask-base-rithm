"""Models for  app."""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class MyTable(db.Model):
    """Playlist."""

    __tablename__ = "mytables"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)
