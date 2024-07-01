from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)
    category = db.Column(db.String(50), nullable=True)

    def __init__(self, description):
        self.description = description
        self.start_time = None
        self.end_time = None
        self.category = None
