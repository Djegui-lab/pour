import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3
# Saisie du nom de l'utilisateur
user_name = st.text_input("Entrez votre nom et prénom")
# Saisie des centres d'intérêt
interests = st.text_area("quel est votre centre d'intérêt ?")
if st.button("Salutation"):
    # Affichage du message de salutation
    if user_name:
       interests_list = interests.split("\n")
       for interest in interests_list:
           st.write(f"Bonjour {user_name} ! merci pour votre analyse. ")
           st.write("je suis un model qui a été fabriquer par Mr.DJEGUI-WAGUÉ.")
           st.write("Votre centre d'intérê est :")
           st.write("- ", interest)
           st.write("")
           st.write("vous êtes la bienvenu(e)",user_name,"!", "vous pouvez continuez à analyser votre base de données dès maintenant ! ")


    else:
        st.write("Veuillez entrer votre nom.")
st.write("AUTEUR : Mr.DJEGUI-WAGUÉ")
st.title('VISUALISATION')
st.subheader("merci pour votre analyse")

uploaded_file = st.file_uploader('Choisir un fichier XLSX ', type='xlsx')
if uploaded_file:
    st.markdown('---')
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    st.title('votre tableau a été telecharger avec succes :')
    statist=df["Age_du_conducteur"]
    st.dataframe(df)
    st.title('ANALYSE DESCRIPTIVE :')
    st.write(df.describe())
    st.write(f" {user_name}  VOUS ETES FORMIDABLE!  ")

    st.title('diagramme à bandes pour age :')
    st.bar_chart(statist)


    groupby_column = st.selectbox(
        "Qu'aimeriez-vous analyser ?",
        ('Nombre_de_sinistres', 'Age_du_conducteur', 'Puissance_fiscale', 'Annees_assurance','Date_de_permis','annee_circulation'),
    )
    # -- GROUP DATAFRAME
    output_columns = ['Annees_assurance', 'Age_du_conducteur']
    df_grouped = df.groupby(by=[groupby_column], as_index=False)[output_columns].mean()
    st.dataframe(df_grouped)
    # -- PLOT DATAFRAME
    fig = px.bar(
        df_grouped,
        x=groupby_column,
        y='Age_du_conducteur',
        color='Annees_assurance',
        color_continuous_scale=['red', 'yellow', 'green'],
        template='plotly_white',
        title=f'<b>age du conducteur & année assurance by {groupby_column}</b>'
    )
    st.plotly_chart(fig)
st.write("")

st.write("")


st.write("Rebonjour encore",user_name,"!","","permettez moi de vous presentez une base de données :")

# Connexion à la base de données SQLite distante
conn = sqlite3.connect('nex_data_assurance.db')

# Charger les données dans un DataFrame
df = pd.read_sql_query('SELECT * FROM nex_data_assurance', conn)

# Afficher les données dans l'interface utilisateur
st.write("base de données pour ",user_name,".")
st.title("votre base de données a l'etat brute")
st.dataframe(df)
st.title(" statistique descriptive de votre base de données")
st.dataframe(df.describe())
st.write("merci pour votre visite", user_name,"!")


