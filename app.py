from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple list to store tasks
tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the task from the form
        task = request.form.get('task')
        if task:
            tasks.append(task)  # Add the task to the list
        return redirect(url_for('index'))

    return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]  # Delete the task at the given index
    return redirect(url_for('index'))

if __name__ == '__main__':
   app.run(host='0.0.0.0')
