from app.models import Aluno, Professor, Disciplina, Nota

alunos = [
    Aluno("Pedro Pedro", 23, "https://github.com/vitorrumke", "https://linkedin.com/in/vitorrumke", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Alfredo Palavro", 20, "https://github.com/vitorrumke", "https://linkedin.com/in/vitorrumke", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Ana Palavro", 18, "https://github.com/vitorrumke", "https://linkedin.com/in/vitorrumke", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Alfredo Jaconi", 19, "https://github.com/vitorrumke", "https://linkedin.com/in/vitorrumke", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Francisco Stedille", 22, "https://github.com/vitorrumke", "https://linkedin.com/in/vitorrumke", "Estudante de Engenharia.", "path/to/photo.jpg"),
]

professores = [
    Professor("Edertec", "https://github.com/anacarolina", "https://linkedin.com/in/anacarolina", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Professor("Rafa", "https://github.com/anacarolina", "https://linkedin.com/in/anacarolina", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Professor("Cris", "https://github.com/anacarolina", "https://linkedin.com/in/anacarolina", "Estudante de Engenharia.", "path/to/photo.jpg"),
]
 
disciplinas = [
    Disciplina("Matemática", professores[0]),
    Disciplina("Física", professores[1]),
    Disciplina("Progamação", professores[0]),
    Disciplina("Games", professores[1]),
    Disciplina("Banco de Dados", professores[2]),
    # Adicione mais disciplinas conforme necessário
]

notas = [
    Nota(alunos[0], disciplinas[0], 9.5),
    Nota(alunos[0], disciplinas[1], 8.0),
    Nota(alunos[0], disciplinas[2], 7.5),
    Nota(alunos[0], disciplinas[3], 6.0),
    Nota(alunos[0], disciplinas[4], 8.5),
    Nota(alunos[1], disciplinas[1], 7.0),
    Nota(alunos[1], disciplinas[2], 7.5),
    Nota(alunos[1], disciplinas[3], 6.0),
    Nota(alunos[1], disciplinas[4], 8.5),
    # Adicione mais notas conforme necessário
]