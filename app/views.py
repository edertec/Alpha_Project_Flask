from flask import render_template, request, redirect, url_for, flash
from app import app
from app.controllers import alunos, professores
from app.models import Aluno, Professor

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/alunos')
def listar_alunos():
    return render_template('listar_alunos.html', alunos=alunos)

@app.route('/professores')
def listar_professores():
    return render_template('professores.html', professores=professores)

@app.route('/alunos/<int:aluno_id>')
def detalhes_aluno(aluno_id):
    aluno = alunos[aluno_id]
    return render_template('detalhes_aluno.html', aluno=aluno)

@app.route('/cadastro_aluno', methods=['GET', 'POST'])
def cadastro_aluno():
    if request.method == 'POST':
        nome = request.form.get('nome')
        idade = request.form.get('idade')
        github = request.form.get('github')
        linkedin = request.form.get('linkedin')
        mini_bio = request.form.get('mini_bio')
        foto = request.form.get('foto')

        if nome and idade and github and linkedin and mini_bio and foto:
            novo_aluno = Aluno(nome, int(idade), github, linkedin, mini_bio, foto)
            alunos.append(novo_aluno)
            flash('Aluno cadastrado com sucesso!', 'success')
            return redirect(url_for('listar_alunos'))
        else:
            flash('Preencha todos os campos!', 'danger')

    return render_template('cadastro_aluno.html')

@app.route('/cadastro_professor', methods=['GET', 'POST'])
def cadastro_professor():
    if request.method == 'POST':
        nome = request.form.get('nome')
        github = request.form.get('github')
        linkedin = request.form.get('linkedin')
        bio = request.form.get('bio')
        foto = request.form.get('foto')

        if nome and github and linkedin and bio and foto:
            novo_professor = Professor(nome, github, linkedin, bio, foto)
            professores.append(novo_professor)
            flash('Professor cadastrado com sucesso!', 'success')
            return redirect(url_for('listar_professores'))
        else:
            flash('Preencha todos os campos!', 'danger')

    return render_template('cadastro_professor.html')

@app.route('/professores/<int:professor_id>')
def detalhes_professor(professor_id):
    professor = professores[professor_id]
    return render_template('detalhes_professor.html', professor=professor)