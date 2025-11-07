import pandas as pd
import streamlit as st
import os

ARQUIVO = "agentes_pastorais.csv"
COLUNAS_PADRAO = [
    "Nome",
    "Função/Cargo",
    "Pastoral",
    "Idade",
    "Tempo de Caminhada",
    "Endereço",
    "Observações",
]
# garante que o caminho do arquivo seja relativo ao arquivo atual (mais robusto em deploys/streamlit)
ARQUIVO_PATH = os.path.join(os.path.dirname(__file__), ARQUIVO)

def carregar_dados():
    if os.path.exists(ARQUIVO_PATH):
        try:
            df = pd.read_csv(ARQUIVO_PATH, encoding="utf-8-sig")
            # valida colunas mínimas (avisa se esquema divergir)
            if not set(COLUNAS_PADRAO).issubset(df.columns):
                st.warning(f"O arquivo '{ARQUIVO}' foi carregado, mas as colunas diferem do esperado.")
            return df
        except Exception as e:
            # mostra erro em Streamlit e retorna DataFrame vazio com as colunas padrões
            st.error(f"Erro ao ler o arquivo '{ARQUIVO}': {e}")
            return pd.DataFrame(columns=COLUNAS_PADRAO)
    else:
        return pd.DataFrame(columns=COLUNAS_PADRAO)


def salvar_dados(df):
    try:
        df.to_csv(ARQUIVO_PATH, index=False, encoding="utf-8-sig")
    except Exception as e:
        st.error(f"Erro ao salvar o arquivo '{ARQUIVO}': {e}")
