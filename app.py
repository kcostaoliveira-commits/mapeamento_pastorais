import streamlit as st
import pandas as pd
from datetime import datetime

# Configurações da página
st.set_page_config(page_title="Mapeamento das Pastorais", page_icon="⛪", layout="wide")

st.title("🎉 Bem-vinda ao Mapeamento de Pastorais!")
st.write("Olha só que fofura... 🎈✨")

# Solta balões animados na tela!
st.balloons()

st.title("📋 Mapeamento dos Agentes das Pastorais")
st.markdown("Sistema simples de cadastro e visualização dos agentes da Igreja Nossa Senhora do Perpétuo Socorro.")

# Função para carregar ou criar a planilha
@st.cache_data
def carregar_dados():
    try:
        # Tenta ler o arquivo Excel.
        df = pd.read_excel("agentes_pastorais.xlsx")
    except FileNotFoundError:
        # Se o arquivo não existir, cria um novo DataFrame com as colunas corretas.
        # ATENÇÃO: As colunas aqui devem refletir as colunas do formulário,
        # mas a leitura do Excel deve ser flexível.
        colunas = ["Nome", "Função/Cargo", "Pastoral", "Idade", "Tempo de Caminhada", "Endereço", "Observações"]
        df = pd.DataFrame(columns=colunas)
        # Salva o DataFrame vazio.
        df.to_excel("agentes_pastorais.xlsx", index=False)
        return df
    except ImportError:
        st.error("ERRO: A biblioteca 'openpyxl' é necessária para ler e escrever arquivos Excel. Por favor, instale-a com 'pip install openpyxl'.")
        colunas = ["Nome", "Função/Cargo", "Pastoral", "Idade", "Tempo de Caminhada", "Endereço", "Observações"]
        df = pd.DataFrame(columns=colunas)
        return df
    
    # **CORREÇÃO FINAL DE NOME DE COLUNA E TIPO DE DADOS:**
    # O problema era que o nome da coluna no Excel ("tempo_de_serviço") era diferente do nome no código ("Tempo de Caminhada").
    # Além disso, o nome da coluna do formulário ("Pastoral") é diferente do Excel ("Pastoral/Grupo").
    
    # 1. Renomear colunas do Excel para o padrão do código (para exibição e salvamento)
    colunas_para_renomear = {
        "tempo_de_serviço": "Tempo de Caminhada",
        "Pastoral/Grupo": "Pastoral",
        "nome": "Nome",
        "endereco": "Endereço",
        "observações": "Observações"
    }
    
    # Inclui a correção anterior de "Carga / mão" caso o arquivo mude.
    if "Carga / mão" in df.columns:
        colunas_para_renomear["Carga / mão"] = "Função/Cargo"
        
    df.rename(columns=colunas_para_renomear, inplace=True)
    
    # 2. Forçar a coluna "Tempo de Caminhada" a ser string (para aceitar "Desde sempre")
    if "Tempo de Caminhada" in df.columns:
        df["Tempo de Caminhada"] = df["Tempo de Caminhada"].astype(str)
        
    # 3. Filtrar apenas as colunas que o aplicativo usa para evitar erros de exibição
    colunas_necessarias = ["Nome", "Função/Cargo", "Pastoral", "Idade", "Tempo de Caminhada", "Endereço", "Observações"]
    df = df.reindex(columns=colunas_necessarias, fill_value=None)
    
    return df

# Carrega os dados
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
    idade = st.number_input("Idade", min_value=0, max_value=120, step=1, format="%d")
    tempo = st.text_input("Tempo de Caminhada (anos)") # Continua sendo um campo de texto
    endereco = st.text_input("Endereço / Bairro")
    observacoes = st.text_area("Observações (opcional)")

    enviar = st.form_submit_button("Salvar")

    if enviar:
        if nome.strip() == "":
            st.warning("⚠️ O campo 'Nome Completo' é obrigatório.")
        else:
            # Cria um novo DataFrame com os dados do formulário
            novo = pd.DataFrame([[nome, funcao, pastoral, idade, tempo, endereco, observacoes]],
                                columns=dados.columns)
            # Concatena o novo registro
            dados = pd.concat([dados, novo], ignore_index=True)
            # Salva a planilha atualizada
            dados.to_excel("agentes_pastorais.xlsx", index=False)
            st.success(f"✅ Agente **{nome}** adicionado com sucesso!")
            st.balloons()
            # st.experimental_rerun()

# Exibir data e rodapé
st.markdown("---")
<<<<<<< HEAD
st.caption(f"🕊️ Atualizado em {datetime.now().strftime('%d/%m/%Y %H:%M')} — Desenvolvido com amor e propósito 💛")
=======
st.caption(f"🕊️ Atualizado em {datetime.now().strftime('%d/%m/%Y %H:%M')} — Desenvolvido com amor e propósito 💛")
>>>>>>> 7923caceb2ab260ccbfc297310e6347b77e49812
