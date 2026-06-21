from flask import Flask, render_template, request, redirect, url_for
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

@app.route("/novo-colaborador", methods=["GET", "POST"])
def novo_colaborador():

    if request.method == "POST":

        colaborador = Colaborador(
            matricula=request.form["matricula"],
            nome=request.form["nome"],
            salario=request.form["salario"],
            email=request.form["email"],
            endereco=request.form["endereco"],
            codigo_dp=request.form["codigo_dp"]
        )
        db.session.add(colaborador)
        db.session.commit()
        
        return redirect(url_for("listar_colaboradores"))

    departamentos = Departamento.query.order_by(
        Departamento.nome
    ).all()

    return render_template(
        "novo_colaborador.html",
        departamentos=departamentos
    )

@app.route("/editar-colaborador/<int:matricula>", methods=["GET", "POST"])
def editar_colaborador(matricula):

    colaborador = Colaborador.query.get_or_404(matricula)

    if request.method == "POST":

        colaborador.nome = request.form["nome"]
        colaborador.salario = request.form["salario"]
        colaborador.email = request.form["email"]
        colaborador.endereco = request.form["endereco"]
        colaborador.codigo_dp = request.form["codigo_dp"]

        db.session.commit()

        return redirect(
            url_for("listar_colaboradores")
        )

    departamentos = Departamento.query.all()

    return render_template(
        "editar_colaborador.html",
        colaborador=colaborador,
        departamentos=departamentos
    )

@app.route("/excluir-colaborador/<int:matricula>")
def excluir_colaborador(matricula):

    colaborador = Colaborador.query.get_or_404(matricula)

    db.session.delete(colaborador)

    db.session.commit()

    return redirect(url_for("listar_colaboradores"))

if __name__ == "__main__":
    app.run(debug=True)
