import streamlit as st
import pandas as pd
import plotly.express as px

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
    st.title('diagramme à bandes pour age :')
    st.bar_chart(statist)


    groupby_column = st.selectbox(
        "Qu'aimeriez-vous analyser ?",
        ('Nombre_de_sinistres', 'Age_du_conducteur', 'Puissance_fiscale', 'Annees_assurance','Date_de_permis','annee_de_mise _en_circulation'),
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


