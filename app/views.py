import matplotlib
matplotlib.use('Agg')  # Use o backend 'Agg' para renderização sem interface gráfica
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from io import BytesIO
import base64
from flask import render_template, request, redirect, url_for, flash
from app import app
from app.controllers import alunos, professores, disciplinas, notas
from app.models import Aluno, Professor, Disciplina, Nota

@app.route('/')
def home():
    # Preparar os dados para visualização
    dados_notas = [{
        'aluno': nota.aluno.nome,
        'disciplina': nota.disciplina.nome,
        'nota': nota.nota
    } for nota in notas]

    dados_alunos = [{
        'nome': aluno.nome,
        'idade': aluno.idade
    } for aluno in alunos]

    df_notas = pd.DataFrame(dados_notas)
    df_alunos = pd.DataFrame(dados_alunos)

    # Dados para o gráfico de barras
    labels = df_notas['disciplina'].unique().tolist()
    data = df_notas.groupby('disciplina')['nota'].mean().tolist()

    # Dados para o histograma
    age_labels = df_alunos['idade'].unique().tolist()
    age_data = df_alunos['idade'].value_counts().sort_index().tolist()

    return render_template('home.html', labels=labels, data=data, age_labels=age_labels, age_data=age_data, notas=notas)


@app.route('/alunos')
def listar_alunos():
    return render_template('listar_alunos.html', alunos=alunos)

@app.route('/professores')
def listar_professores():
    return render_template('listar_professores.html', professores=professores)

@app.route('/alunos/<int:aluno_id>')
def detalhes_aluno(aluno_id):
    aluno = alunos[aluno_id]
    return render_template('detalhes_aluno.html', aluno=aluno)

@app.route('/professores/<int:professor_id>')
def detalhes_professor(professor_id):
    professor = professores[professor_id]
    return render_template('detalhes_professor.html', professor=professor)

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

@app.route('/cadastro_nota', methods=['GET', 'POST'])
def cadastro_nota():
    if request.method == 'POST':
        aluno_id = int(request.form.get('aluno_id'))
        disciplina_id = int(request.form.get('disciplina_id'))
        nota = float(request.form.get('nota'))

        nova_nota = Nota(alunos[aluno_id], disciplinas[disciplina_id], nota)
        notas.append(nova_nota)
        flash('Nota cadastrada com sucesso!', 'success')
        return redirect(url_for('visualizar_estatisticas'))

    return render_template('cadastro_nota.html', alunos=alunos, disciplinas=disciplinas)

@app.route('/estatisticas')
def visualizar_estatisticas():
    # Preparar os dados para visualização
    dados_notas = [{
        'aluno': nota.aluno.nome,
        'disciplina': nota.disciplina.nome,
        'nota': nota.nota
    } for nota in notas]

    dados_alunos = [{
        'nome': aluno.nome,
        'idade': aluno.idade
    } for aluno in alunos]

    df_notas = pd.DataFrame(dados_notas)
    df_alunos = pd.DataFrame(dados_alunos)

    # Gráfico de Barras: Média das notas por disciplina
    fig, ax = plt.subplots()
    df_notas.groupby('disciplina')['nota'].mean().plot(kind='bar', ax=ax)
    ax.set_title('Média das Notas por Disciplina')
    ax.set_ylabel('Média das Notas')
    img_barras = BytesIO()
    plt.savefig(img_barras, format='png')
    img_barras.seek(0)
    plot_url_barras = base64.b64encode(img_barras.getvalue()).decode('utf8')

    # Histograma: Distribuição das idades dos alunos
    fig, ax = plt.subplots()
    df_alunos['idade'].plot(kind='hist', bins=10, ax=ax)
    ax.set_title('Distribuição das Idades dos Alunos')
    ax.set_xlabel('Idade')
    img_hist = BytesIO()
    plt.savefig(img_hist, format='png')
    img_hist.seek(0)
    plot_url_hist = base64.b64encode(img_hist.getvalue()).decode('utf8')

    # Boxplot: Notas por Disciplina
    fig, ax = plt.subplots()
    sns.boxplot(x='disciplina', y='nota', data=df_notas, ax=ax)
    ax.set_title('Distribuição das Notas por Disciplina')
    img_boxplot = BytesIO()
    plt.savefig(img_boxplot, format='png')
    img_boxplot.seek(0)
    plot_url_boxplot = base64.b64encode(img_boxplot.getvalue()).decode('utf8')

    return render_template('estatisticas.html', 
                           plot_url_barras=plot_url_barras, 
                           plot_url_hist=plot_url_hist, 
                           plot_url_boxplot=plot_url_boxplot)
