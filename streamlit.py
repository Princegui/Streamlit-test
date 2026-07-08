import streamlit
import streamlit as st 


st.title("Parlons des SIG")
st.header("Introduction aux SIG")
st.subheader("Comprendre les Systèmes d'Informations Géographiques")
st.text("Systèmes d'Informations Géographiques ?")


st.set_page_config(
    page_title="My App",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("# SIG :red[Tutorial]")
st.markdown("## :green[Importance des SIG]")
st.markdown("### 🌐💻 Web Applications")
st.markdown("""
> _"Les Systèmes d'Informations Géographiques (*SIG*) sont de puissants outils d'aides à la *décision*."
>
> **Khayri R.R. Woulfe**
""")


html_string = """
<p style='font-family:courier;color:red'>Streamlit accepts:</p>

<ul>
    <li> Built-in text elements </li>
    <li> Markdown </li>
    <li> HTML </li>
</ul>
"""

st.markdown(html_string, unsafe_allow_html=True)


# Bouttons et cage à cocher

widget = st.radio(
    "Which widget do you prefer?",
    ["Button", "Checkbox"]
)

st.write("Here's your widget")

if widget == "Button":
    if st.button("Show", type="primary"):
        # Perform what you want
        pass
else:
    if st.checkbox("Afficher"):
        # Perform what you want
        pass


# Pour les avoir comme menu
st.sidebar.title("Parlons des SIG")
st.sidebar.header("Introduction aux SIG")

option = st.selectbox(
    "Choisis ton outil de travail",
    ('QGIS', 'ArcGis Pro', 'Magrit')
)

my_dict = {"profit": "15500$", "Revenu": "30800$", "Losses": "3%"}

# my_dict= {"Profit": "15500$", "Revenue": "30800$", "Losses": "3%"}

Options = st.multiselect(
    'Select the metrics to analyze',
    ['Profit', 'Revenue', 'Losses'])

# Calibrage etr définition du temps

from datetime import datetime, time

# simple slider
age = st.slider('How old are you?', 0, 130, 25)
st.write("You are", age, "years old")

# range slider
values = st.slider('Select a range of values',
                   0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# range time slider
#from datetime import date
import datetime

# Correct: uses the module's date class
my_date = datetime.date(2024, 3, 14) 

start_time = st.slider(
    "When you want start?",
    value=datetime.date(2020, 9, 30),
    format="MM/DD//YY - hh:mm")
st.write("Start:", start_time)


name = st.text_input('Your name', placeholder="Name Surname")
number = st.number_input('Select how many orders you want to show', min_value=1, value=3)
date = st.date_input(
    "Select the date range",
    value=(datetime.date(2023, 1, 1), datetime.date(2023, 1, 15)))

# Soumission des infos calibrées
with st.form("form"):
    st.subheader("Data entry form")
    product = st.text_input("Product name:")
    data = st.date_input("Release date:", value=datetime.datetime(2023, 1, 1))
    
    price = st.slider("Product price :blue[(euro)]:", 1, 2000)
    status = st.radio("Status:", ("Available", "Not Available"))
    
    # Every form must have a submit button
    submitted = st.form_submit_button("Submit")

if submitted:
    st.success("You have listed this product:")
    st.write({"Product": product, "Release date": data.strftime('%d/%m/%Y'), "Price": price, "Status": status})


################################## PARTIE 2 #####################################################

# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np


# # 1. Titre de l'application
# st.title("Mon application Streamlit : Visualisation de CSV")

# # 2. Importer le fichier CSV
# uploaded_file = st.file_uploader("D:/cours_M1/streamlit_diop/bouake.csv", type="csv")

# if uploaded_file is not None:
#     # index_col=0 permet d'ignorer la première colonne de numéros (0, 1, 2)
#     df = pd.read_csv(uploaded_file, sep=';', index_col=0)
    
#     # Afficher un aperçu du tableau
#     st.write("Aperçu des données :")
#     st.dataframe(df)
        
#         # 3. Tracer un graphique
#     st.write("Graphique : Comparaison des statistiques par Paramètre")

#     # Configuration des barres pour Matplotlib
#     parametres = df["id"].tolist()
#     x = np.arange(len(parametres))  # Positions des groupes sur l'axe X
#     largeur = 0.25                  # Largeur de chaque barre

#     # Créer le tracé avec Matplotlib
#     fig, ax = plt.subplots(figsize=(8, 5))

#     # Tracer les trois barres côte à côte pour chaque paramètre
#     ax.bar(x - largeur, df["blesse"], label="blesse", color="#1f77b4")
#     ax.bar(x, df["Population"], label="Population", color="#ff7f0e")
#     ax.bar(x + largeur, df["acc"],  label="acc", color="#d62728")

#     # Personnalisation des axes
#     ax.set_xlabel("id")
#     ax.set_ylabel("Valeur (°C)")
#     ax.set_title("blesse, acc et Population  par accident")
#     ax.set_xticks(x)
#     ax.set_xticklabels(parametres)
#     ax.legend()
#     ax.grid(axis='y', linestyle='--', alpha=0.7)

#     # Afficher le graphique sur streamlit
#     st.pyplot(fig)

# #########interactive##############
# import folium
# import streamlit as st
# from streamlit_folium import st_folium
# from typing import Any


# st.header("Folium Maps on Streamlit")
# m_draw: folium.Map = folium.Map(
#     location=[14.497401, -14.452362]  # Coordonnées du Sénégal
# )

# output: Any = st_folium(
#     m_draw,
#     width=700,
#     height=500
# )


# # INITIALISATION EARTH ENGINE

# import ee
# import geemap

# try:
#     ee.Initialize(project="ee-kanemareme13")
# except Exception:
#     ee.Authenticate()
#     ee.Initialize(project="ee-kanemareme13")