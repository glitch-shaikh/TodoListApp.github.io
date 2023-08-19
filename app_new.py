from flask import Flask, render_template, request, redirect
from database import Database

app = Flask(__name__)
db = Database()

@app.route('/')
def index():
    tasks = db.get_task()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    db.insert_task(task)
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    db.delete_task(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
