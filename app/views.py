from flask import render_template, request
from app import app
from app.controllers import alunos

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/alunos')
def listar_alunos():
    return render_template('listar_alunos.html', alunos=alunos)

@app.route('/alunos/<int:aluno_id>')
def detalhes_aluno(aluno_id):
    aluno = alunos[aluno_id]
    return render_template('detalhes_aluno.html', aluno=aluno)