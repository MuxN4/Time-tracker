from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Task

@app.route('/')
def home():
    tasks = Task.query.all()
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