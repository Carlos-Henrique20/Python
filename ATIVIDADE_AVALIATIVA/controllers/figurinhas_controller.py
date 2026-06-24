from flask import Blueprint, redirect, render_template, request, url_for

from models import Colecionador, Figurinha, ItemOferta, OfertaTroca, db

figurinhas_bp = Blueprint("figurinhas", __name__, url_prefix="/figurinhas")


@figurinhas_bp.route("/")
def index():
    ofertas = OfertaTroca.listar_com_colecionador()
    return render_template("figurinhas/lista_ofertas.html", ofertas=ofertas)


@figurinhas_bp.route("/oferta/cadastrar", methods=["GET", "POST"])
def cadastrar_oferta():
    colecionadores = Colecionador.listar()
    figurinhas = Figurinha.listar()

    if request.method == "POST":
        try:
            colecionador_id = int(request.form.get("colecionador_id", 0))
            figurinha_oferece_id = int(request.form.get("figurinha_oferece_id", 0))
            figurinha_deseja_id = int(request.form.get("figurinha_deseja_id", 0))
        except ValueError:
            return render_template(
                "figurinhas/formulario_oferta.html",
                colecionadores=colecionadores,
                figurinhas=figurinhas,
                erro="Seleção inválida.",
            )

        observacao = request.form.get("observacao", "").strip()

        if not colecionador_id or not figurinha_oferece_id or not figurinha_deseja_id:
            return render_template(
                "figurinhas/formulario_oferta.html",
                colecionadores=colecionadores,
                figurinhas=figurinhas,
                erro="Selecione colecionador e as duas figurinhas.",
            )

        if figurinha_oferece_id == figurinha_deseja_id:
            return render_template(
                "figurinhas/formulario_oferta.html",
                colecionadores=colecionadores,
                figurinhas=figurinhas,
                erro="A figurinha oferecida e a desejada não podem ser iguais.",
            )

        OfertaTroca.criar_com_itens(colecionador_id, figurinha_oferece_id, figurinha_deseja_id, observacao)
        return redirect(url_for("figurinhas.index"))

    return render_template(
        "figurinhas/formulario_oferta.html",
        colecionadores=colecionadores,
        figurinhas=figurinhas,
    )
