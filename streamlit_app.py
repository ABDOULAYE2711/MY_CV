import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# ABDOULAYE BADJI
##### *Resume* 
''')

image = Image.open('badji.png')
st.image(image, width=150)

st.markdown('## Profil', unsafe_allow_html=True)
st.info('''
Très à l’aise avec les chiffres et les statistiques, l’analyse de données est un domaine qui me passionne. 
M’avoir dans votre entreprise, c’est la renforcer par ma rigueur, ma curiosité et ma grande capacité d’adaptation. 
Ma priorité est de respecter les délais et de rendre un travail parfait.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">ABDOULAYE BADJI</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Profile <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#formations">FORMARTIONS</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#experiences-professionnelles">EXPERIENCES PROFESSIONNELLES</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#references">Références</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## FORMATIONS
''')
txt('**Maîtrise Économie Appliquée**',
'**2008-2009**')
st.markdown('''
`Université Gaston Berger, Saint Louis`
''')

txt('**Licence Economique Appliquée**',
'**2006-2007**')
st.markdown('''
`Université Gaston Berger, Saint Louis`
''')

txt('**DEUG II Science Economies et Gestions**',
'**2005-2006**')
st.markdown('''
`Université Gaston Berger, Saint Louis`
''')


#####################
st.markdown('''
## EXPERIENCES PROFESSIONNELLES
''')

txt('**Data Quality and Assurance Officer**',
"**01/2022 - Aujourd'hui**")
txt('*SHELTER FOR LIFE, Ziguinchor*',
"")
st.markdown('''
- Programmation de formulaire CATI avec TaroWorks. 
- Extraction, apurement et traitement de données.
- Conception de rapports et tableaux de bord avec Salesforce.
''')

txt('**Chargé de traitement de données**',
"**08/2021 - 12/2021**")
txt('*LA VOIX DU CLIENT (SAT), Dakar*',
"")
st.markdown('''
- Programmation de formulaire CATI et CAWI avec ASKIA DESIGN. 
- Mise en forme et contrôle de base de données.
- Edition de tri à plat et Tri croisé.
- Recherche permanent de méthodes pour fiabiliser les données et optimiser les contrôles.
''')

txt('**Data Analyst**',
"**06/2019 - 07/2021**")
txt('*SUNNA MOON SUARL, Ziguinchor*',
"")
st.markdown('''
- Extraction, traitement et analyse des données.
- Assuré la bonne interprétation et la diffusion des rapports d’analyse.
- Conception de tableau de bord avec PowerBI.
''')

txt('**Agent statisticien**',
"**07/2015 - 05/2019**")
txt('*OMEDIA - GROUP, Dakar*',
"")
st.markdown('''
- Gestion d’études quantitatives et rôle de field manager.
- Conception de formulaire CATI et CAMI.
- Apurement et traitement de données.
''')

txt('**Auditeur Junior**',
"**07/2013 - 06/2015**")
txt('*ICONIA DATA SEARCH, Abidjan*',
"")
st.markdown('''
- Retails Audit des appareils électroménagers et électroniques à Dakar.
''')

txt('**Superviseur terrain**',
"**04/2013 - 05/2013**")
txt('*CABINET CIBLE, Douala*',
"")
st.markdown('''
- Former et encadrer les enquêteurs sur le terrain.
- Gérer les outils et matériels de collecte.
- Contrôler et transférer les données vers le serveur.
''')

txt('**Prestataire de services**',
"**01/2010 - 03/2013**")
txt('*KANTAR TNS, Dakar*',
"")
st.markdown('''
- Contrôle qualité et cohérence des données.
- Codification et saisie des données.
''')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `SPSS`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `ggplot2`, `PowerBI`, `Tableaux`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `R Shiny`, `Heroku`')
txt3('Forms', '`Net-servey`, `ASKIA DESIGN`, `TaroWorks`, `Kobotoolbox`')
#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/abdoulaye-badji-a24697a0/')
txt2('GitHub', 'https://github.com/ABDOULAYE2711')
txt2('Youtube', 'https://www.youtube.com/channel/UCZ_Sor5J6415zV8k3hNlk6Q')

#####################
st.markdown('''
## Références
''')
txt4('Mr Antoine Sebastianutti', 'Directeur Général Moon', 'antoine@moon.community')
txt4('Mr Arnaud Moisan', 'Directeur Associé Omedia', 'amoisan@omedia-group.com')
txt4('Mr Christophe Gondry', 'Directeur Associé Omedia','cgondry@omedia-group.com')

star_rating1 = ":star:" * 5
star_rating2 = ":star:" * 3
st.sidebar.write("**LANGUES**")
st.sidebar.write("*Français*")
st.sidebar.write(f"{star_rating1}")
st.sidebar.write("*Angais*")
st.sidebar.write(f"{star_rating2}")
