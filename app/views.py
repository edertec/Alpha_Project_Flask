from flask import render_template
from app import app
from app.controllers import alunos

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/alunos')
def listar_alunos():
    return render_template('listar_alunos.html', alunos=alunos)