from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Task, TimeEntry
from datetime import datetime, timedelta

@app.route('/')
def home():
    tasks = Task.query.all()
    for task in tasks:
        total_time = timedelta()
        for entry in task.time_entries:
            if entry.end_time:
                total_time += entry.end_time - entry.start_time
            else:
                total_time += datetime.utcnow() - entry.start_time
        task.total_time = total_time
    return render_template('home.html', tasks=tasks)

@app.route('/add_task', methods=['GET','POST'])
def add_task():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        new_task = Task(name=name, description=description)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_task.html')

@app.route('/start_time/<int:task_id>', methods=['POST'])
def start_time(task_id):
    new_time_entry = TimeEntry(task_id=task_id, start_time=datetime.utcnow())
    db.session.add(new_time_entry)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/stop_time/<int:entry_id>', methods=['POST'])
def stop_time(entry_id):
    time_entry = TimeEntry.query.get(entry_id)
    if time_entry and time_entry.end_time is None:
        time_entry.end_time = datetime.utcnow()
        db.session.commit()
    return redirect(url_for('home'))