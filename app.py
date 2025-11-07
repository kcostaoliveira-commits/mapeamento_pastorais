import streamlit as st
import pandas as pd
from datetime import datetime

# Configurações da página
st.set_page_config(page_title="Mapeamento das Pastorais", page_icon="⛪", layout="wide")

st.title("📋 Mapeamento dos Agentes das Pastorais")
st.markdown("Sistema simples de cadastro e visualização dos agentes da Comunidade São Francisco de Assis.")

# Função para carregar ou criar a planilha
@st.cache_data
def carregar_dados():
    try:
        df = pd.read_excel("agentes_pastorais.xlsx")
    except FileNotFoundError:
        colunas = ["Nome", "Função/Cargo", "Pastoral", "Idade", "Tempo de Caminhada", "Endereço", "Observações"]
        df = pd.DataFrame(columns=colunas)
        df.to_excel("agentes_pastorais.xlsx", index=False)
    return df

dados = carregar_dados()

# Mostrar tabela
st.subheader("👥 Lista de Agentes Cadastrados")
st.dataframe(dados, use_container_width=True)

# Formulário para novo cadastro
st.subheader("➕ Adicionar Novo Agente")

with st.form("form_agente"):
    nome = st.text_input("Nome Completo")
    funcao = st.text_input("Cargo / Função")
    pastoral = st.text_input("Pastoral / Grupo")
    idade = st.number_input("Idade", min_value=0, max_value=120, step=1)
    tempo = st.text_input("Tempo de Caminhada (anos)")
    endereco = st.text_input("Endereço / Bairro")
    observacoes = st.text_area("Observações (opcional)")

    enviar = st.form_submit_button("Salvar")

    if enviar:
        if nome.strip() == "":
            st.warning("⚠️ O campo 'Nome Completo' é obrigatório.")
        else:
            novo = pd.DataFrame([[nome, funcao, pastoral, idade, tempo, endereco, observacoes]],
                                columns=dados.columns)
            dados = pd.concat([dados, novo], ignore_index=True)
            dados.to_excel("agentes_pastorais.xlsx", index=False)
            st.success(f"✅ Agente **{nome}** adicionado com sucesso!")
            st.balloons()

# Exibir data e rodapé
st.markdown("---")
st.caption(f"🕊️ Atualizado em {datetime.now().strftime('%d/%m/%Y %H:%M')} — Desenvolvido por Kali com amor e propósito 💛")
