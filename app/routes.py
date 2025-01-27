from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, Task

main_bp = Blueprint('main', __name__)

# Página inicial
@main_bp.route('/')
def index():
    return render_template('index.html')

# Página de lista de tarefas
@main_bp.route('/tarefas')
def tasks_page():
    tasks = Task.query.all()
    return render_template('tarefas.html', tasks=tasks)

# Adicionar nova tarefa
@main_bp.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('título')
    description = request.form.get('descrição')
    if title:
        new_task = Task(title=title, description=description)
        db.session.add(new_task)
        db.session.commit()
        flash('Tarefa adicionada com sucesso!', 'success')
    else:
        flash('O título da tarefa é obrigatório!', 'error')
    return redirect(url_for('main.tasks_page'))

# Atualizar status de uma tarefa
@main_bp.route('/update/<int:task_id>')
def update_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.completed = not task.completed
        db.session.commit()
        flash('Tarefa atualizada com sucesso!', 'success')
    else:
        flash('Tarefa não encontrada!', 'error')
    return redirect(url_for('main.tasks_page'))

# Deletar uma tarefa
@main_bp.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        flash('Tarefa deletada com sucesso!', 'success')
    else:
        flash('Tarefa não encontrada!', 'error')
    return redirect(url_for('main.tasks_page'))
