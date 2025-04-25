import os

import pandas as pd
import plotly.express as px
import plotly.io as pio
from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, url_for
from models import Gastos, db  # Importa o `db` criado no models.py

load_dotenv()
app = Flask(__name__, template_folder="template")

# Configurações
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.getenv("SECRET_KEY")

# Inicializa o banco
db.init_app(app)


@app.route("/")
def index():
    # Obter os gastos do banco de dados
    gastos = Gastos.query.all()
    total_gasto = sum(gasto.valor for gasto in gastos)

    # Converter os gastos para um DataFrame Pandas
    data = [
        {
            "Data": gasto.data,
            "Categoria": gasto.categoria,
            "Valor": gasto.valor,
            "Descricao": gasto.descricao,
        }
        for gasto in gastos
    ]

    df = pd.DataFrame(data)
    if "Data" in df.columns:
        df_gasto_dia = df.groupby(["Data"])["Valor"].sum().reset_index()
    else:
        df_gasto_dia = pd.DataFrame(columns=["Data", "Valor"])

    # Criar um gráfico de linha com Plotly
    fig = px.line(
        df_gasto_dia,
        x="Data",
        y="Valor",
        title="Despesas por Dia",
        labels={"Data": "Data", "Valor": "Total Gasto (R$)"},
        log_y=True,
    )

    if not df.empty and "Categoria" in df.columns:
        df_pie = df.groupby("Categoria")["Valor"].sum().reset_index()
    else:
        df_pie = pd.DataFrame(columns=["Categoria", "Valor"])

    fig2 = px.pie(
        df_pie,
        names="Categoria",
        values="Valor",
        title="Maiores Categorias",
        labels={"Categoria": "Categoria", "Valor": "Total Gasto (R$)"},
    )
    # Converter o gráfico para HTML

    graph_html2 = pio.to_html(fig2, full_html=False)
    graph_html = pio.to_html(fig, full_html=False)

    return render_template(
        "index.html",
        gastos=gastos,
        total_gasto=total_gasto,
        graph_html=graph_html,
        graph_html2=graph_html2,
    )


@app.route("/add_despesa", methods=["POST"])
def add_gastos():
    if request.method == "POST":
        data = request.form["data"]
        categoria = request.form["categoria"]
        valor = request.form["valor"]
        descricao = request.form["descricao"]
        if not data or not categoria or not valor or not descricao:
            flash("Por favor, preencha todos os campos.", "error")

        novo_gasto = Gastos(
            data=data, categoria=categoria, valor=valor, descricao=descricao
        )
        db.session.add(novo_gasto)
        db.session.commit()
        return redirect(url_for("index"))


@app.route("/remover/<int:id>", methods=["POST"])
def remover_gasto(id):
    gasto = Gastos.query.get(id)
    if gasto:
        db.session.delete(gasto)
        db.session.commit()
        flash("Gasto removido com sucesso!", "success")
    else:
        flash("Gasto não encontrado.", "error")
    return redirect(url_for("index"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
