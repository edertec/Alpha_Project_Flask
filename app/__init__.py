from flask import Flask

app = Flask(__name__)

# Defina a chave secreta
app.secret_key = 'edertex'

from app import views
