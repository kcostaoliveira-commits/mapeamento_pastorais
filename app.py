import pandas as pd
import streamlit as st
import os

ARQUIVO = "agentes_pastorais.csv"

def carregar_dados():
    if os.path.exists(ARQUIVO):
        try:
            return pd.read_csv(ARQUIVO)
        except:
            return pd.DataFrame(columns=["Nome", "Função/Cargo", "Pastoral", "Idade", "Tempo de Caminhada", "Endereço", "Observações"])
    else:
        return pd.DataFrame(columns=["Nome", "Função/Cargo", "Pastoral", "Idade", "Tempo de Caminhada", "Endereço", "Observações"])

def salvar_dados(df):
    df.to_csv(ARQUIVO, index=False, encoding="utf-8")
