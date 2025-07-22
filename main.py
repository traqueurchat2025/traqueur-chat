import streamlit as st
import datetime

st.title("🛡️ Traqueur-Chat – Détection de comportements suspects")

# Liste de mots-clés à risque
mots_dangereux = [
    "photo nue", "toute nue", "viens chez moi", "tu es seule",
    "tu dors", "envoie une photo", "sexy", "tu as quel âge", "je t'aime"
]

# Analyse du texte
def analyser(conversation):
    conversation = conversation.lower()
    score = 0
    signes = []

    for mot in mots_dangereux:
        if mot in conversation:
            score += 10
            signes.append(mot)

    niveau = "vert"
    if score >= 30:
        niveau = "rouge"
    elif score >= 10:
        niveau = "orange"

    return score, niveau, signes

# Interface utilisateur
texte = st.text_area("Colle ici la conversation à analyser")

if st.button("Analyser"):
    if texte.strip() == "":
        st.warning("Veuillez coller une conversation.")
    else:
        score, niveau, signes = analyser(texte)
        st.metric("Score de dangerosité", f"{score}/100")
        st.write(f"**Niveau de risque :** {niveau.upper()}")
        st.write("**Signes détectés :**")
        for s in signes:
            st.write(f"- {s}")
