import streamlit as st

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

st.title("Hello Geeks")
st.header("Ce site est fait...")
st.subheader("Pour les Geeks !!!")
st.text("Bienvenue à tous les Geeks")
st.markdown("### Bienvenue à tous les joueur Clash Royale et Brawl Star")
st.success("Bravo")
st.info("Nouvelle mise à jour clash royal disponible dans 2 jours")
st.warning("Uniquement pour les joueurs de clash royale")
st.error("la mise à jour est reportée de 3 jours")
st.write("Bienvenue à tous les geeks avec commande write")
from PIL import Image
img = Image.open("image/clash_royale")
st.image(img, width=200)
st.header("De quelle jeux voulez-vous savoir la prochaine mise à jour ?")
if st.checkbox("Brawl Star"):
	st.write("Mise à jour disponible dans 10 jours.")
if st.checkbox("Clash Royale"):
	st.write("Mise à jour disponible dans 5 jours.")
status = st.radio("Vous êtes un joueur de:",("Brawl Star","Clash Royale","Les deux"))
if(status == "Brawl Star"):
	st.success("Vos actualités seront majoritairement à propos de Brawl Star")
if(status == "Clash Royale"):
	st.success("Vos actualités seront majoritairement à propos de Clash Royale")
if(status == "Les deux"):
	st.success("Vos actualités seront à propos des deux")
raison = st.selectbox("Vous consulter ce site pour:",
	["Regarder les tournois", "Lire les actualités", "Avoir des informations sur les mises à jours", "Les trois"])
st.write("Vous consulter ce site pour", raison)
raisons = st.multiselect("Vous consulter de site pour:",
	["Regarder les tournois", "Lire les actualités", "Avoir des informations sur les mises à jours"])
st.write("Vous consulter ce site pour", len(raisons), "raisons.")
name = st.text_input("Nom")
level = st.slider("Depuis combien de temps jouer vous à Brawl Star ou Clash Royale?",1, 5)
st.text("Depuis {} ans.".format(level))
if(st.button("Sauvegarder les réponses")):
	st.success("Réponses sauvegarder avec succès!")


st.title("Calculatrice")
if(st.button("1")):
	st.write("1",end = "")
