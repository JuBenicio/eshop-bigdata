import streamlit as st
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["eshop"]
collection = db["clientes"]

st.title("📊 E-Shop Brasil - Gestão de Dados")
st.header("➕ Inserir Cliente")
nome = st.text_input("Nome")
email = st.text_input("Email")
if st.button("Salvar"):
    if nome and email:
        collection.insert_one({"nome": nome, "email": email})
        st.success("Cliente inserido com sucesso!")

st.header("📋 Clientes Cadastrados")
clientes = list(collection.find())
for c in clientes:
    st.write(f"{c['nome']} - {c['email']}")