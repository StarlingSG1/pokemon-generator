import streamlit as st
import pandas as pd
import requests

st.title("Générer un pokemon en fonction de ses statistiques")

st.header("Donnez les statistiques du pokemon")
type = st.selectbox("Type", ["Feu", "Eau", "Électrique"])
group = st.selectbox("Groupe", ["Souris", "Dragon", "Graine", "Oiseau"])
legendary = st.checkbox("Légendaire")
attack = st.number_input("Attaque", min_value=0, max_value=1000, value=50)
attack_special = st.number_input("Attaque Spéciale", min_value=0, max_value=1000, value=50)
defence = st.number_input("Defense", min_value=0, max_value=100, value=85)
defence_special = st.number_input("Defense Spéciale", min_value=0, max_value=100, value=85)
description = st.text_area("Description", value="Il est gros, fort, rouge avec un air méchant. Mais il est lent.", height=100)

if st.button("Générer pokémon"):
    generation_data = {
        type,
        group,
        legendary,
        attack,
        attack_special,
        defence,
        defence_special,
        description
    }
