import math
from flask import render_template, request


def calcular():
    try:
        num1 = float(request.form["num1"])
    except (ValueError, KeyError):
        return render_template("calculadora.html", etapas="Informe um número válido.", resultados="")

    operacao = request.form.get("operacao", "+")

    # ── Raiz quadrada (só usa num1) ──────────────────────────────────────────
    if operacao == "sqrt":
        if num1 < 0:
            etapas = f"Não existe raiz real de {num1}."
            resultado = "Erro: número negativo"
        else:
            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado}"

    # ── Logaritmo (log10 de num1) ────────────────────────────────────────────
    elif operacao == "log":
        if num1 <= 0:
            etapas = f"Logaritmo indefinido para {num1}."
            resultado = "Erro: número deve ser positivo"
        else:
            resultado = math.log10(num1)
            etapas = f"log₁₀({num1}) = {resultado}"

    # ── Operações binárias (precisam de num2) ────────────────────────────────
    else:
        num2_valor = request.form.get("num2", "").strip()
        if not num2_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o segundo número para esta operação.",
                resultados="",
            )

        try:
            num2 = float(num2_valor)
        except ValueError:
            return render_template("calculadora.html", etapas="Segundo número inválido.", resultados="")

        if operacao == "+":
            resultado = num1 + num2
            etapas = f"{num1} + {num2} = {resultado}"

        elif operacao == "-":
            resultado = num1 - num2
            etapas = f"{num1} − {num2} = {resultado}"

        elif operacao == "*":
            resultado = num1 * num2
            etapas = f"{num1} × {num2} = {resultado}"

        elif operacao == "/":
            if num2 == 0:
                etapas = "Divisão por zero não é permitida."
                resultado = "Erro: divisão por zero"
            else:
                resultado = num1 / num2
                etapas = f"{num1} ÷ {num2} = {resultado}"

        elif operacao == "**":
            resultado = num1 ** num2
            etapas = f"{num1} ^ {num2} = {resultado}"

        else:
            etapas = "Operação desconhecida."
            resultado = "Erro"

    return render_template("calculadora.html", etapas=etapas, resultados=resultado)
