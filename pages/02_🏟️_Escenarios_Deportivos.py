# Cargar datos
import streamlit as st
import pandas as pd
import pydeck as pdk
import plotly.express as px
import plotly.graph_objects as go
import base64


st.set_page_config(layout="wide")

# Título principal, h1 denota el estilo del título 1
st.markdown("<h1 style='text-align: center; color: red;'>🏟️ ESCENARIOS DEPORTIVOS EN COLOMBIA 🏟️</h1>", unsafe_allow_html=True)

from PIL import Image
background = Image.open('escenario.jpg')
col1, col2, col3 = st.columns([0.17, 5, 0.27])
col2.image(background, width=1138)


df= pd.read_csv('Consolidado_Escenarios (1).csv')
df0= df.drop(["urlimagen","email","codigo","direccion","paginaweb","telefono"], axis=1)
df0= df0.rename(columns={"tipo":"CLASIFICACIÓN","nombre":"NOMBRE DEL ESCENARIO","deporte":"DEPORTE","municipio":"MUNICIPIO","departamento":"DEPARTAMENTO","ubicacion":"UBICACIÓN","razonsocial":"RAZÓN SOCIAL","claseubicacion":"TIPO ZONA","localidadcomuna":"COMUNA","descripcion":"TIPO DE ESCENARIO","latitud":"LATITUD","longitud":"LONGITUD"})
df0["DEPORTE"]=df0["DEPORTE"].replace({"Recreativo":"Recreativo y Deportivo","Deportivo":"Recreativo y Deportivo","Recreativo y Educación Fisíca":"Recreativo y Deportivo","FISICOCULTURISMO":"FISICULTURISMO","TENIS DE CAMPO":"TENIS","ARQUEROS DE COLOMBIA":"TIRO Y CAZA"})
df0["UBICACIÓN"]=df0["UBICACIÓN"].replace({"Caja de compensaci?":"Otro","Universidad o centro de educaci? superior":"Universidad"})
df0["TIPO ZONA"]=df0["TIPO ZONA"].replace({"nan":"Zona Rural"})
df0["TIPO DE ESCENARIO"]=df0["TIPO DE ESCENARIO"].replace({"CAMPO DE TENIS":"CANCHA DE TENIS","SALA DE TENIS":"CANCHA DE TENIS","CANCHA DE TENIS DE CAMPO":"CANCHA DE TENIS","CANCHA DE TENIS N? 2":"CANCHA DE TENIS","CANCHA DE TENIS N? 1":"CANCHA DE TENIS","CANCHA DE MULTIPLE":"CANCHA MULTIPLE",
    "CANCHA DE MICROFUTBOL (FUTBOL DE SALON)":"CANCHA DE MICROFUTBOL","CANCHA DE MICROFUTBOL N? 2":"CANCHA DE MICROFUTBOL","CANCHA DE VOLEIBOL COLISEO":"CANCHA DE VOLEIBOL","CANCHA MICROFUTBOL":"CANCHA DE MICROFUTBOL","PISTA DE PATINAJE VELOCIDAD":"PISTA DE PATINAJE","CANCHA DE BALONCESTO PLACA CUBIERTA":"CANCHA DE BALONCESTO",
    "CANCHA DE TENIS N? 6":"CANCHA DE TENIS","CANCHS MULTIPLE":"CANCHA MULTIPLE","CANCHA VOLEIBOL":"CANCHA DE VOLEIBOL","POLIDEPORTIVO":"CANCHA MULTIPLE","COLISEO MAYOR":"CANCHA MULTIPLE","CANCHA SINTETICA DE FUTBOL 8":"CANCHA FUTBOL 8","CANCHA MULTIPLE N? 2":"CANCHA MULTIPLE","CANCHA MULTIPLE N? 1":"CANCHA MULTIPLE","CANCHA DE FUTBOL N? 2":"CANCHA DE FUTBOL",
    "CANCHA DE FUTBOL N? 1":"CANCHA DE FUTBOL","CANCHA DE TENIS POLVO DE LADRILLO":"CANCHA DE TENIS","CANCHA DE TENIS N? 7":"CANCHA DE TENIS","CANCHA DE MICRIFUTBOL":"CANCHA DE MICROFUTBOL","CANCHA MULTIPLE (MEDIA ESTRUCTURA)":"CANCHA MULTIPLE","CANCHA DE TENIS N? 4":"CANCHA DE TENIS","PISTAS PARA LA PRACTICA DE PATINAJE":"PISTA DE PATINAJE","CANCHA DE VOLEIBOL CUBIERTA":"CANCHA DE VOLEIBOL","CANCHA DE BALONCESTO COLISEO":"CANCHA DE BALONCESTO",
    "COLISEO CUBIERTO":"COLISEO","CANCHA FUTBOL 8":"CANCHA DE FUTBOL","CANCHA DE TENIS N? 3":"CANCHA DE TENIS","CANCHA DE TENIS N? 5":"CANCHA DE TENIS","PATINODROMO":"PISTA DE PATINAJE","SALAS PARA LA PRACTICA DE TAEKWONDO":"SALON DE TAEKWONDO","CANCHA DE MICROFUTBOL FOTO 030":"CANCHA DE MICROFUTBOL","CANCHA MULTIPLE PLACA CUBIERTA":"CANCHA MULTIPLE","CANCHA MULTIPLE N?1":"CANCHA MULTIPLE",
    "COLISEO CUBIERTO SAN JORGE":"COLISEO","CANCHA DE VOLEIBOL PLACA CUBIERTA":"CANCHA DE VOLEIBOL","CANCHA AUXILIAR DE MICROFUTBOL":"CANCHA DE MICROFUTBOL","CANCHA SINTETICA DE MICROFUTBOL":"CANCHA DE MICROFUTBOL","CANCHA AUXILIAR DE VOLEIBOL":"CANCHA DE VOLEIBOL", 'ESTADIO MENOR DE BEISBOL ""JOSE VARGAS"':"DIAMANTE DE BEISBOL","SALON DE BILLAR Y TENIS DE MESA":"SALA DE TENIS DE MESA","CANCHA MULTIPLE CUBIERTA":"CANCHA MULTIPLE","CANCHA DE TENIS INFANTIL":"CANCHA DE TENIS","SALON DE TENIS":"CANCHA DE TENIS",
    "CANCHA MICROFUTBOL PLACA CUBIERTA":"CANCHA DE MICROFUTBOL","SALON DE TENIS DE MESA":"SALA DE TENIS DE MESA","DIAMANTE DE SOFTBOL":"CAMPO DE SOFTBOL","SALAS O SALONES PARA LA PRACTICA DE GIMNASIA":"SALON DE GIMNASIA OLIMPICA","PISTA DE ATLETISMO EN ASFALTO":"PISTA DE ATLETISMO","COLISEO DE GIMNASIA":"SALON DE GIMNASIA OLIMPICA","SALON DE GIMNASIA RITMICA":"SALON DE GIMNASIA OLIMPICA","CAMPO DE BEISBOL":"CANCHA DE BEISBOL","SALON DE SQUASH":"CANCHA DE SQUASH",
    "COLISEO DE JUDO":"SALON DE JUDO","DIAMANTE DE BEISBOL":"CANCHA DE BEISBOL","COLISEO DE BOLOS":"SALON DE BOLOS","SALA DE TAEKWONDO":"SALON DE TAEKWONDO","CAMPO PARA PESCA":"DEPORTES DE MAR","PISTA  DE TROTE":"PISTA DE TROTE","ESTADIO DE FUTBOL":"CANCHA DE FUTBOL","PISTADE BICICROSS":"PISTA DE BICICROSS","GIMNASIO DE PESAS":"GIMNASIO","GIMNASIOS PARA LA PRACTICA DE CULTURA FISICA":"GIMNASIO","CANCHA MUTIPLE":"CANCHA MULTIPLE","SALON DE LEVANTAMIENTO DE PESAS":"GIMNASIO",
    "CANCHA DE SOFTBOL":"CAMPO DE SOFTBOL","CAMPO DE HOCKEY":"CANCHA DE HOCKEY","PISCINAINFANTIL":"PISCINA INFANTIL","SALONES DE AJEDREZ":"SALA DE AJEDREZ","TENIS DE MESA":"SALA DE TENIS DE MESA","CANCHA MULTPLE":"CANCHA MULTIPLE"})


st.markdown("<h3 style='text-align: center; color: gray;'> ¿QUÉ DEPARTAMENTO TIENE MAYOR NÚMERO DE ESCENARIOS? </h3>", unsafe_allow_html=True)

df_d=df0[["DEPARTAMENTO","LONGITUD","LATITUD","NOMBRE DEL ESCENARIO"]]

st.write(pdk.Deck( # Código para crear el mapa
    
    # Set up del mapa
    map_style='mapbox://styles/mapbox/dark-v10',
    initial_view_state={
        'latitude' : df_d['LATITUD'].mean(),
        'longitude': df_d['LONGITUD'].mean(),
        'zoom' : 5,
        'pitch': 50
        },
    
    # Capa con información
    layers = [pdk.Layer(
        'HexagonLayer',
        data = df_d[['NOMBRE DEL ESCENARIO','LATITUD','LONGITUD']],
        get_position = ['LONGITUD','LATITUD'],
        radius = 10000,
        extruded = True,
        elevation_scale = 100,
        elevation_range = [0,1000])]
    ))



c1, c2= st.columns((1,1))

c1.markdown("<h3 style='text-align: center; color: gray;'> TOP 10 DEPARTAMENTOS CON MAYOR NÚMERO DE ESCENARIOS </h3>", unsafe_allow_html=True)

df_d2 = df_d.groupby(['DEPARTAMENTO'])[['NOMBRE DEL ESCENARIO']].count().reset_index().sort_values('NOMBRE DEL ESCENARIO',ascending=False).rename(columns = {'NOMBRE DEL ESCENARIO':'CANTIDAD DE ESCENARIOS'}).head(10)

fig = px.bar(df_d2, x='DEPARTAMENTO', y='CANTIDAD DE ESCENARIOS', color = 'DEPARTAMENTO',
             color_discrete_map={'VALLE DEL CAUCA':'darkturquoise','BOLIVAR':'green','ATLANTICO':'grey','RISARALDA':'forestgreen','BOYACA':'red','BOGOTÁ D.C.':'yellow','CUNDINAMARCA':'turquoise','CORDOBA':'royalblue','CALDAS':'gold','ANTIOQUIA':'lawngreen'},
             width=650, height=500)

# Editar gráfica
fig.update_layout(showlegend=False,
        title_x=0.5,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        template = 'simple_white',
        xaxis_title="<b>DEPARTAMENTO<b>",
        yaxis_title='<b>FRECUENCIA<b>',
        legend_title_text=''
        
            )

# Enviar gráfica a streamlit
c1.plotly_chart(fig)

#------------------------------------SEGUNDO ANALISIS

c2.markdown("<h3 style='text-align: center; color: gray;'> ¿QUÉ TIPO DE ZONA ES EN LA QUE MÁS PREDOMINAN LOS ESCENARIOS DEPORTIVOS? </h3>", unsafe_allow_html=True)

df_3=df0[["TIPO ZONA","DEPARTAMENTO"]].fillna("Zona Rural")

base = df_3.groupby(['TIPO ZONA'])[['DEPARTAMENTO']].count().reset_index()

fig = px.pie(base , values = 'DEPARTAMENTO', names = 'TIPO ZONA', color='TIPO ZONA',
             color_discrete_map={'Zona Urbana':'red','Zona Rural':'silver'},
             
             title = '<b>% Escenarios deportivos por zona<b>')

# agregar detalles a la gráfica
fig.update_layout(
    template = 'plotly_dark',
    legend_title = 'Tipo de Zona',
    title_x = 0.5,
    
    legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="right",
            x=0.8))

c2.plotly_chart(fig)


#---------------------------- TERCER ANALISIS

st.markdown("<h3 style='text-align: center; color: gray;'> ⚽🏀¿QUÉ DEPORTE TIENE MAYOR NÚMERO DE ESCENARIOS?🏐🏉 </h3>", unsafe_allow_html=True)


df_4=df0[["DEPORTE","DEPARTAMENTO"]]

df_4 = df_4[df_4['DEPORTE'].notnull()]

df_4 = df_4.groupby(['DEPORTE'])[['DEPARTAMENTO']].count().reset_index().sort_values('DEPARTAMENTO',ascending=False).head(15)

df_5= df_4.drop([49],axis=0)

df_d5 = df_5.groupby(['DEPORTE'])[['DEPARTAMENTO']].count().reset_index().sort_values('DEPARTAMENTO',ascending=False)

# crear gráfica
fig = px.bar(df_5, x='DEPORTE', y='DEPARTAMENTO', color = 'DEPORTE',  
             color_discrete_map={'KARATE DO':'ghostwhite','PARAPENTE':'navy','TENIS':'lime','NATACION':'deepskyblue','TEJO':'dimgray','BOXEO':'red','VOLEIBOL':'royalblue','BALONCESTO':'darkorange','FUTBOL DE SALON':'lawngreen','PATINAJE':'darkviolet','ATLETISMO':'gold','TAEKWONDO':'darkred','CICLISMO':'slateblue','FUTBOL':'springgreen'},
             title ='<b><b>', width=1200, height=550)

# agregar detalles a la gráfica
fig.update_layout(showlegend=False,
    xaxis_title = 'Deportes',
    yaxis_title = 'Numero de escenarios',
    template = 'simple_white',
    title_x = 0.5,
    legend_title = '',
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
        
            )

st.plotly_chart(fig)
