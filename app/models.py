from app import db
from datetime import datetime

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Task {self.name}>'
    
class TimeEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    task = db.relationship('Task', backref=db.backref('time_entries', lazy='dynamic'))

    def __repr__(self):
        return f'<TimeEntry {self.id} for Task {self.task_id}>'