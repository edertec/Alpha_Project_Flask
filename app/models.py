class Aluno:
    def __init__(self, nome, idade, github, linkedin, mini_bio, foto):
        self.nome = nome
        self.idade = idade
        self.github = github
        self.linkedin = linkedin
        self.mini_bio = mini_bio
        self.foto = foto

class Professor:
    def __init__(self, nome, github, linkedin, bio, foto):
        self.nome = nome
        self.github = github
        self.linkedin = linkedin
        self.bio = bio
        self.foto = foto

class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

class Nota:
    def __init__(self, aluno, disciplina, nota):
        self.aluno = aluno
        self.disciplina = disciplina
        self.nota = nota