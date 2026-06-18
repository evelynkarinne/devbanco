from flask import Flask, render_template
from config import Config
from models import db, Departamento, Colaborador
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/departamentos")
def listar_departamentos():

    departamentos = Departamento.query.all()

    return render_template(
        "departamentos.html",
        departamentos=departamentos
    )


@app.route("/colaboradores")
def listar_colaboradores():

    colaboradores = Colaborador.query.all()

    return render_template(
        "colaboradores.html",
        colaboradores=colaboradores
    )

if __name__ == "__main__":
    app.run(debug=True)
