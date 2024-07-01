from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Task
from utils import categorize_task
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/tasks', methods=['POST'])
def create_task():
    description = request.json.get('description')
    task = Task(description=description)
    task.category = categorize_task(description)
    db.session.add(task)
    db.session.commit()
    return jsonify({'id': task.id, 'description': task.description, 'category': task.category}), 201

@app.route('/tasks/<int:task_id>/start', methods=['POST'])
def start_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    task.start_time = datetime.utcnow()
    db.session.commit()
    return jsonify({'id': task.id, 'start_time': task.start_time.isoformat()}), 200

@app.route('/tasks/<int:task_id>/stop', methods=['POST'])
def stop_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    task.end_time = datetime.utcnow()
    db.session.commit()
    return jsonify({'id': task.id, 'end_time': task.end_time.isoformat()}), 200

@app.route('/tasks/<int:task_id>/summary', methods=['GET'])
def task_summary(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    if not task.start_time or not task.end_time:
        return jsonify({'error': 'Task has not been completed'}), 400
    duration = task.end_time - task.start_time
    return jsonify({'id': task.id, 'description': task.description, 'duration': str(duration), 'category': task.category}), 200

if __name__ == '__main__':
    app.run(debug=True)
