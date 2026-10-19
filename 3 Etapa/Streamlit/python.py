import streamlit as st
import pandas as pd

st.title(" Sistema de Padaria")
st.header("Monte o seu pedido abaixo!")

st.write("Bem-vindo a minha padaria.")

st.write("____________________________________________________________________________________________________________________")

cardapio_dados = {
    "Item": ["Pão de Sal", "Pão de Queijo", "Croissant", "Bolo de Cenoura", "Café Express", "Suco de Laranja"],
    "Preço (R$)": [0.50, 2.50, 4.50, 12.00, 3.00, 5.00]
}
df_cardapio = pd.DataFrame(cardapio_dados)

st.write("###  Nosso Cardápio:")
st.write(df_cardapio)

st.write("____________________________________________________________________________________________________________________")

st.write("###  Escolha seus produtos:")

itens_selecionados = st.multiselect(
    "Selecione os itens que deseja comprar:", 
    df_cardapio["Item"].tolist()
)

forma_entrega = st.selectbox("Como deseja receber seu pedido?", ["Comer no local", "Para viagem", "Entregar em casa"])
st.write("Opção de entrega selecionada: ", forma_entrega)

st.write("____________________________________________________________________________________________________________________")

col1, col2 = st.columns([1, 1])

col1.write("###  Defina as quantidades:")

total_pedido = 0.0

with col1.form("fechar_pedido"):
    quantidades = {}
    
    for item in itens_selecionados:
        quantidades[item] = st.number_input(f"Quantidade de {item}:", min_value=1, value=1, step=1)
    
    comprar = st.form_submit_button(" Calcular Total")

if comprar:
    if not itens_selecionados:
        col2.error("Por favor, selecione pelo menos um item no campo acima!")
    else:
        col2.write("###  Resumo do Pedido:")
        
        for item in itens_selecionados:
            preco_unitario = df_cardapio.loc[df_cardapio["Item"] == item, "Preço (R$)"].values[0]
            qtd = quantidades[item]
            subtotal = preco_unitario * qtd
            total_pedido += subtotal
            
            col2.write(f"- {qtd}x {item}: R$ {subtotal:.2f}")
        
        col2.write("---")
        col2.title(f"Total: R$ {total_pedido:.2f}")
