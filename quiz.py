import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

st.title("📋 Générateur de quiz")
st.info("Donne un sujet, je génère un quiz QCM dessus.")

sujet = st.text_input("Sujet du quiz :")
nb_questions = st.slider("Nombre de questions :", 3, 10, 5)

if st.button("Générer le quiz"):
    if sujet.strip() == "":
        st.warning("Écris un sujet avant de générer !")
    else:
        prompt = f"""Génère un quiz QCM de {nb_questions} questions sur le sujet : {sujet}.
Pour chaque question, donne 4 options (A, B, C, D) et indique la bonne réponse à la fin.
Format clair et structuré en markdown."""

        try:
            reponse = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )
            st.markdown(reponse.choices[0].message.content)
        except Exception as e:
            st.error(f"Une erreur est survenue : {e}")