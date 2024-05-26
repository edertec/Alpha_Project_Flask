# Projeto Flask Alunos

Este é um projeto de exemplo utilizando o framework Flask para listar alunos em uma matriz colorida e animada. O objetivo é demonstrar a arquitetura de 3 camadas (Model-View-Controller) e fornecer uma base para projetos futuros.

## Estrutura do Projeto

```
flask_aluno_project/
├── app/
│   ├── __init__.py
│   ├── controllers.py
│   ├── models.py
│   ├── static/
│   │   ├── styles.css
│   ├── templates/
│   │   ├── home.html
│   │   ├── listar_alunos.html
│   ├── views.py
├── .gitignore
├── run.py
├── README.md
```

- **`app/__init__.py`**: Inicializa a aplicação Flask.
- **`app/controllers.py`**: Controla a lógica do negócio e cria instâncias de alunos.
- **`app/models.py`**: Define o modelo de dados `Aluno`.
- **`app/static/`**: Contém arquivos estáticos como CSS e JavaScript.
- **`app/templates/`**: Contém os templates HTML.
- **`app/views.py`**: Define as rotas e as views da aplicação.
- **`run.py`**: Arquivo de execução do servidor Flask.
- **`.gitignore`**: Arquivo que especifica quais arquivos e diretórios devem ser ignorados pelo Git.
- **`README.md`**: Este arquivo que você está lendo.

## Pré-requisitos

- Python 3.x
- pip (Python package installer)

## Como Baixar e Rodar o Projeto

### Passo 1: Clonar o Repositório

Clone o repositório para a sua máquina local usando o seguinte comando no terminal:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### Passo 2: Criar um Ambiente Virtual

Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

### Passo 3: Instalar as Dependências

Instale as dependências necessárias usando o pip:

```bash
pip install -r requirements.txt
```

### Passo 4: Rodar o Servidor de Desenvolvimento

Inicie o servidor Flask:

```bash
python run.py
```

### Passo 5: Acessar a Aplicação

Abra o navegador e vá para `http://127.0.0.1:5000/` para ver a página de boas-vindas. Para ver a lista de alunos, vá para `http://127.0.0.1:5000/alunos`.

## Explicação do Projeto

### Modelo (Model)

O modelo `Aluno` é definido no arquivo `app/models.py` e representa a estrutura dos dados dos alunos.

### Visão (View)

As views são definidas no arquivo `app/views.py` e controlam o que é exibido ao usuário. Existem duas rotas principais:
- `/`: Exibe a página de boas-vindas.
- `/alunos`: Exibe a lista de alunos.

### Controlador (Controller)

O controlador `app/controllers.py` gerencia a lógica do negócio e cria instâncias de `Aluno` para serem exibidas na view.

### Estilos e Animações

Os estilos CSS e animações são definidos no arquivo `app/static/styles.css` e utilizam o Bootstrap e a biblioteca Animate.css para criar um design moderno e responsivo.

## Contribuições

Se quiser contribuir com o projeto, por favor, faça um fork do repositório, crie uma branch para suas alterações e envie um pull request.

1. Faça um fork do projeto.
2. Crie uma branch para suas alterações (`git checkout -b feature/aluno-novo`).
3. Commit suas alterações (`git commit -am 'Add new feature'`).
4. Push para a branch (`git push origin feature/aluno-novo`).
5. Abra um pull request.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
```

### 1. Adicionar o `requirements.txt`

Para garantir que todos os pacotes necessários sejam instalados, crie um arquivo `requirements.txt` na raiz do projeto e adicione as dependências necessárias:

```bash
Flask==2.0.1
```

Para gerar este arquivo, você pode rodar o seguinte comando após instalar todas as dependências:

```bash
pip freeze > requirements.txt
```