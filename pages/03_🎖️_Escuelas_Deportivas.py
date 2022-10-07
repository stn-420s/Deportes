# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 18:04:46 2022

@author: Luis Mejía
"""

import streamlit as st 
import pandas as pd
import pydeck as pdk
import plotly
import datetime
from datetime import datetime
import matplotlib as plt
import plotly.express as px
from plotly.subplots import make_subplots
import matplotlib.pyplot as plot 
import seaborn as sns 
import plotly.graph_objects as go 

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; color: red ;'>ESCUELAS DEPORTIVAS</h1>", unsafe_allow_html=True)
from PIL import Image
background = Image.open('des.jpeg')
col1, col2, col3 = st.columns([1, 2, 1])
col2.image(background)
#Cargar base de datos
pd.set_option('display.max_columns', None)
df=pd.read_csv('Programa_Escuelas_Deportivas_Para_Todos.csv')


#df['OCCUR_DATE'] = pd.to_datetime(df['OCCUR_DATE'], format = '%m/%d/%Y') # convertir fecha en formato datetime
#df['OCCUR_TIME'] = pd.to_datetime(df['OCCUR_TIME'], format = '%H:%M:%S') # convertir hora en formato datetime
#df['YEAR'] = df['OCCUR_DATE'].dt.year
#df['HOUR'] = df['OCCUR_TIME'].dt.hour
#df['YEARMONTH'] = df['OCCUR_DATE'].dt.strftime('%y%m')
#df.columns = df.columns.map(str.lower) # convertir en minusculas

#Homologacion categorias de la variable Departamento
df['Departamento']= df['Departamento'].replace(['AMAZONAS'],'Amazonas')
df['Departamento']= df['Departamento'].replace(['ANTIOQUIA'],'Antioquia')
df['Departamento']= df['Departamento'].replace(['ARAUCA'],'Arauca')
df['Departamento']= df['Departamento'].replace(['ATLÁNTICO','ATLANTICO'],'Atlántico')
df['Departamento']= df['Departamento'].replace(['BOLÍVAR','BOLIVAR'],'Bolívar')
df['Departamento']= df['Departamento'].replace(['BOYACÁ'],'Boyacá')
df['Departamento']= df['Departamento'].replace(['CALDAS'],'Caldas')
df['Departamento']= df['Departamento'].replace(['CAQUETA'],'Caquetá')
df['Departamento']= df['Departamento'].replace(['CASANARE'],'Casanare')
df['Departamento']= df['Departamento'].replace(['CAUCA'],'Cauca')
df['Departamento']= df['Departamento'].replace(['CESAR'],'Cesar')
df['Departamento']= df['Departamento'].replace(['CHOCÓ','CHOCO'],'Chocó')
df['Departamento']= df['Departamento'].replace(['CÓRDOBA','CORDOBA'],'Córdoba')
df['Departamento']= df['Departamento'].replace(['CUNDINAMARCA'],'Cundinamarca')
df['Departamento']= df['Departamento'].replace(['Guanía','GUAINÍA','GUAINIA'],'Guainía')
df['Departamento']= df['Departamento'].replace(['GUAVIARE'],'Guaviare')
df['Departamento']= df['Departamento'].replace(['HUILA'],'Huila')
df['Departamento']= df['Departamento'].replace(['LA GUAJIRA'],'La Guajira')
df['Departamento']= df['Departamento'].replace(['META'],'Meta')
df['Departamento']= df['Departamento'].replace(['NARIÑO'],'Nariño')
df['Departamento']= df['Departamento'].replace(['NORTE DE SANTANDER','Norte de santander'],'Norte de Santander')
df['Departamento']= df['Departamento'].replace(['PUTUMAYO','putumayo'],'Putumayo')
df['Departamento']= df['Departamento'].replace(['QUINDIO'],'Quindío')
df['Departamento']= df['Departamento'].replace(['SANTANDER'],'Santander')
df['Departamento']= df['Departamento'].replace(['SUCRE'],'Sucre')
df['Departamento']= df['Departamento'].replace(['TOLIMA','tolima'],'Tolima')
df['Departamento']= df['Departamento'].replace(['VALLE DEL CAUCA'],'Valle del Cauca')
df['Departamento']= df['Departamento'].replace(['VAUPÉS'],'Vaupés')
df['Departamento']= df['Departamento'].replace(['VICHADA'],'Vichada')
df['Departamento']= df['Departamento'].replace(['San Andrés , Providencia'],'San Andrés')

#Homologacion categorias variable Municipio
df['Municipio']= df['Municipio'].replace(['LETICIA','leticia'],'Leticia')
df['Municipio']= df['Municipio'].replace(['puerto nariño','PUERTO NARIÑO'],'Puerto Nariño')
df['Municipio']= df['Municipio'].replace(['APARTADÓ', 'APARTADO', 'Apartado'],'Apartadó')
df['Municipio']= df['Municipio'].replace(['CAMPAMENTO'],'Campamento')
df['Municipio']= df['Municipio'].replace(['CAREPA'],'Carepa') 
df['Municipio']= df['Municipio'].replace(['CHIGORODO'], 'Chigorodó')
df['Municipio']= df['Municipio'].replace(['EL BAGRE'],'El bagre')
df['Municipio']= df['Municipio'].replace(['SABANALARGA','sabanalarga'],'Sabanalarga')
df['Municipio']= df['Municipio'].replace(['san carlos'],'San Carlos')
df['Municipio']= df['Municipio'].replace(['SAN PEDRO', 'san pedro','San pedro'],'San Pedro')
df['Municipio']= df['Municipio'].replace(['SANTA BARBARA','santa barbara'],'Santa Bárbara')
df['Municipio']= df['Municipio'].replace(['ZARAGOZA','zaragoza'],'Zaragoza')
df['Municipio']= df['Municipio'].replace(['ARAUCA'],'Arauca')
df['Municipio']= df['Municipio'].replace(['ARAUQUITA','arauquita'],'Arauquita')
df['Municipio']= df['Municipio'].replace(['CRAVO NORTE'],'Cravo Norte')
df['Municipio']= df['Municipio'].replace(['FORTUL','fortul'],'Fortul')
df['Municipio']= df['Municipio'].replace(['PUERTO RONDÓN'],'Puerto Rondón')
df['Municipio']= df['Municipio'].replace(['SARAVENA'],'Saravena')
df['Municipio']= df['Municipio'].replace(['PALMAR DE VARELA','palmar de varela'],'Palmar de Varela')
df['Municipio']= df['Municipio'].replace(['REPELON','Repelon','REPELÓN'],'Repelón')
df['Municipio']= df['Municipio'].replace(['SABANAGRANDE'],'Sabanagrande')
df['Municipio']= df['Municipio'].replace(['SANTA LUCÍA','Santa lucia','SANTA LUCIA'],'Santa Lucia')
df['Municipio']= df['Municipio'].replace(['SUAN','suan'],'Suan')
df['Municipio']= df['Municipio'].replace(['TUBARÀ','TUBARA','TUBARÁ'],'Tubará')
df['Municipio']= df['Municipio'].replace(['CALAMAR'],'Calamar')
df['Municipio']= df['Municipio'].replace(['CARMEN DE BOLIVAR','EL CARMEN DE BOLIVAR'],'El carmen de bolivar')
df['Municipio']= df['Municipio'].replace(['el guamo','EL GUAMO','GUAMO'],'El Guamo')
df['Municipio']= df['Municipio'].replace(['MARÍA LA BAJA','MARIA LA BAJA'],'Maria la baja')
df['Municipio']= df['Municipio'].replace(['SAN JACINTO'],'San Jacinto Bolivar')
df['Municipio']= df['Municipio'].replace(['SAN JACINTO DEL CAUCA'],'San Jacinto del Cauca')
df['Municipio']= df['Municipio'].replace(['SAN JUAN NEPOMUCENO'],'San Juan Nepomuceno')
df['Municipio']= df['Municipio'].replace(['MOMPOX','MomPOX','mompox'],'Mompox')
df['Municipio']= df['Municipio'].replace(['VILLANUEVA','villanueva'],'Villanueva')
df['Municipio']= df['Municipio'].replace(['ZAMBRANO','zambrano'],'Zambrano')
df['Municipio']= df['Municipio'].replace(['BUENAVISTA','buenavista'],'Buenavista')
df['Municipio']= df['Municipio'].replace(['CERINZA','cerinza'],'Cerinza')
df['Municipio']= df['Municipio'].replace(['CÓMBITA'],'Cómbita')
df['Municipio']= df['Municipio'].replace(['MARIPI','maripi'],'Maripi')
df['Municipio']= df['Municipio'].replace(['MIRAFLORES'],'Miraflores')
df['Municipio']= df['Municipio'].replace(['LA PAZ','la paz','La paz','la Paz'],'La Paz')
df['Municipio']= df['Municipio'].replace(['SOTAQUIRA'],'Sotaquira')
df['Municipio']= df['Municipio'].replace(['TIBASOSA','tibasosa'],'Tibasosa')
df['Municipio']= df['Municipio'].replace(['SAN JOSÉ DEL GUAVIARE','SAN JOSÉ','San Jose'],'San Jose del Guaviare')
df['Municipio']= df['Municipio'].replace(['ALBANIA','albania'],'Albania')
df['Municipio']= df['Municipio'].replace(['BELEN DE LOS ANDAQUIES','BELÉN DE LOS ANDAQUÍES'],'Belén de los Andaquíes')
df['Municipio']= df['Municipio'].replace(['cartagena del chaira','CARTAGENA DEL CHAIRÁ'],'Cartagena del Chairá')
df['Municipio']= df['Municipio'].replace(['PUERTO RICO'],'Puerto Rico')
df['Municipio']= df['Municipio'].replace(['LA SALINA'],'La Salina')
df['Municipio']= df['Municipio'].replace(['NUNCHIA','Nunchia'],'Nunchía')
df['Municipio']= df['Municipio'].replace(['OROCUE - RESGUARDO INDIGENA SAN JUANITO','OROCUE'],'Orocué')
df['Municipio']= df['Municipio'].replace(['SAN LUIS DE PALENQUE'],'San Luis de Palenque')
df['Municipio']= df['Municipio'].replace(['TRINIDAD','trinidad'],'Trinidad')
df['Municipio']= df['Municipio'].replace(['guachene','GUACHENE','Guachene'],'Guachené')
df['Municipio']= df['Municipio'].replace(['puerto tejada','Puerto tejada','PUERTO TEJADA'],'Puerto Tejada')
df['Municipio']= df['Municipio'].replace(['santander de quilichao','SANTANDER DE QUILICHAO','santander de Quilichao','Santander de Q'],'Santander de Quilichao')
df['Municipio']= df['Municipio'].replace(['Piendamo'],'Piendamó')
df['Municipio']= df['Municipio'].replace(['POPAYAN','POPAYÁN','Popayan'],'Popayán')
df['Municipio']= df['Municipio'].replace(['LA VEGA','la vega'],'La Vega')
df['Municipio']= df['Municipio'].replace(['MERCADERES'],'Mercaderes')
df['Municipio']= df['Municipio'].replace(['INZA'],'Inzá')
df['Municipio']= df['Municipio'].replace(['JAMBALÓ','Jambalò'],'Jambaló')
df['Municipio']= df['Municipio'].replace(['CHIMICHAGUA','chimichagua'],'Chimichagua')
df['Municipio']= df['Municipio'].replace(['san alberto','SAN ALBERTO'],'San Alberto')
df['Municipio']= df['Municipio'].replace(['San Martin','san martin','SAN MARTIN','SAN MARTÍN'],'San Martín')
df['Municipio']= df['Municipio'].replace(['PELAYA','pelaya'],'Pelaya')
df['Municipio']= df['Municipio'].replace(['GAMARRA','gamarra'],'Gamarra')
df['Municipio']= df['Municipio'].replace(['manaure','MANAURE'],'Manaure')
df['Municipio']= df['Municipio'].replace(['TAMALAMEQUE','tamalameque'],'Tamalameque')
df['Municipio']= df['Municipio'].replace(['SAN DIEGO','san diego'],'San Diego')
df['Municipio']= df['Municipio'].replace(['LA GLORIA','la gloria'],'La Gloria')
df['Municipio']= df['Municipio'].replace(['ACANDI'],'Acandí')
df['Municipio']= df['Municipio'].replace(['ALTO BAUDÓ','ALTO BAUDO'],'Alto Baudó')
df['Municipio']= df['Municipio'].replace(['ATRATO YUTO','ATRATO'],'Atrato')
df['Municipio']= df['Municipio'].replace(['BAHÍA SOLANO'],'Bahía solano')  
df['Municipio']= df['Municipio'].replace(['BOJAYA'],'BOJAYÁ')   
df['Municipio']= df['Municipio'].replace(['CERTEGUI'],'Certegui')
df['Municipio']= df['Municipio'].replace(['CARMEN DEL DARIEN'],'Carmen del Darien')
df['Municipio']= df['Municipio'].replace(['El Carmen de Atrato Choco','Carmen del Carmen','El Carmen de Atrato Choco l','CARMEN DE ATRATO'],'El Carmen de Atrato')
df['Municipio']= df['Municipio'].replace(['ISTMINA','istmina'],'Istmina')
df['Municipio']= df['Municipio'].replace(['MEDIO BAUDO'],'MEDIO BAUDÓ')
df['Municipio']= df['Municipio'].replace(['MEDIO SANJUAN','M. SAN JUAN'],'MEDIO SAN JUAN')
df['Municipio']= df['Municipio'].replace(['NOVITA'],'Novita')
df['Municipio']= df['Municipio'].replace(['Nuqui','nuqui'],'NUQUÍ')
df['Municipio']= df['Municipio'].replace(['QUIBDÓ','QUIBDÓ - TAGACHI','QUIBDO','Quibdo','quibdò'],'Quibdó')
df['Municipio']= df['Municipio'].replace(['SAN JOSÉ DEL PALMAR','SAN JOSE DEL PALMAR'],'San Jose del Palmar')
df['Municipio']= df['Municipio'].replace(['sipi','Sipi'],'Sipí')
df['Municipio']= df['Municipio'].replace(['UNGUIA','UNGUÍA'],'Unguía')
df['Municipio']= df['Municipio'].replace(['CANALETE','canalete'],'Canalete') 
df['Municipio']= df['Municipio'].replace(['CHINU'],'Chinú')
df['Municipio']= df['Municipio'].replace(['cotorra','COTORRA'],'Cotorra')
df['Municipio']= df['Municipio'].replace(['LOS CÓRDOBAS','LOS CORDOBAS','LOS  CORDOBAS'],'Los Córdobas')
df['Municipio']= df['Municipio'].replace(['MOÑITOS','moñitos'],'Moñitos')
df['Municipio']= df['Municipio'].replace(['puerto escondido','Puerto escondido'],'Puerto Escondido')
df['Municipio']= df['Municipio'].replace(['PURISIMA'],'Purisima')
df['Municipio']= df['Municipio'].replace(['SAN ANTERO','San antero'],'San Antero')
df['Municipio']= df['Municipio'].replace(['SAN PELAYO'],'San Pelayo')
df['Municipio']= df['Municipio'].replace(['LORICA','lorica'],'Lorica')
df['Municipio']= df['Municipio'].replace(['SESQUILE','sesquile'],'Sesquile')
df['Municipio']= df['Municipio'].replace(['GUATAQUI'],'Guataqui')
df['Municipio']= df['Municipio'].replace(['SUPATÁ','supata'],'Supata')
df['Municipio']= df['Municipio'].replace(['UBALA'],'Ubala')
df['Municipio']= df['Municipio'].replace(['SAN JUAN DE RIOSECO','san de Rioseco'],'San Juan de Rioseco')
df['Municipio']= df['Municipio'].replace(['CHIPAQUE'],'Chipaque')
df['Municipio']= df['Municipio'].replace(['fosca','FOSCA'],'Fosca')
df['Municipio']= df['Municipio'].replace(['La palma'],'La Palma')
df['Municipio']= df['Municipio'].replace(['zipacon'],'Zipacon')
df['Municipio']= df['Municipio'].replace(['SAN BERNARDO'],'San Bernardo')
df['Municipio']= df['Municipio'].replace(['San Antonio Del Tequendama','san antonio del tequendama','San Antonio Del tequendama','san Antonio Del Tequendama','san Antonio del Tequendama'],'San Antonio del Tequendama')
df['Municipio']= df['Municipio'].replace(['INIRIDA'],'Inirida')
df['Municipio']= df['Municipio'].replace(['EL RETORNO','El RETORNO','RETORNO','Retorno'],'El Retorno')
df['Municipio']= df['Municipio'].replace(['algeciras','ALGECIRAS'],'Algeciras')
df['Municipio']= df['Municipio'].replace(['campoalegre','CAMPOALEGRE'],'Campoalegre')
df['Municipio']= df['Municipio'].replace(['tello','TELLO'],'Tello')
df['Municipio']= df['Municipio'].replace(['AGRADO','agrado'],'Agrado')
df['Municipio']= df['Municipio'].replace(['GIGANTE'],'Gigante')
df['Municipio']= df['Municipio'].replace(['SUAZA','suaza'],'Suaza')
df['Municipio']= df['Municipio'].replace(['LA ARGENTINA'],'La Argentina')
df['Municipio']= df['Municipio'].replace(['LA PLATA'],'La Plata')
df['Municipio']= df['Municipio'].replace(['NATAGA'],'Nataga')
df['Municipio']= df['Municipio'].replace(['TESALIA'],'Tesalia')
df['Municipio']= df['Municipio'].replace(['BARRANCAS'],'Barrancas')
df['Municipio']= df['Municipio'].replace(['DISTRACCION'],'Distraccion')
df['Municipio']= df['Municipio'].replace(['FONSECA','fonseca'],'Fonseca')
df['Municipio']= df['Municipio'].replace(['HATONUEVO','Hato Nuevo','HATO NUEVO'],'Hatonuevo')
df['Municipio']= df['Municipio'].replace(['URUMITA'],'Urumita')
df['Municipio']= df['Municipio'].replace(['ARACATACA'],'Aracataca')
df['Municipio']= df['Municipio'].replace(['EL BANCO'],'El Banco')
df['Municipio']= df['Municipio'].replace(['GUAMAL','guamal'],'Guamal')
df['Municipio']= df['Municipio'].replace(['PUEBLO VIEJO','pueblo viejo'],'Pueblo Viejo')
df['Municipio']= df['Municipio'].replace(['CABUYARO','cabuyaro'],'Cabuyaro')
df['Municipio']= df['Municipio'].replace(['CUBARRAL'],'Cubarral')
df['Municipio']= df['Municipio'].replace(['El dorado','EL DORADO','el dorado'],'El Dorado')
df['Municipio']= df['Municipio'].replace(['MALAMBO','malambo'],'Malambo')
df['Municipio']= df['Municipio'].replace(['GUAMAL','guamal'],'Guamal')
df['Municipio']= df['Municipio'].replace(['la macarena','LA MACARENA'],'La Macarena')
df['Municipio']= df['Municipio'].replace(['MESETAS','mesetas'],'Mesetas')
df['Municipio']= df['Municipio'].replace(['RESTREPO','restrepo'],'Restrepo')
df['Municipio']= df['Municipio'].replace(['SAN JUANITO'],'San Juanito')

#Homologacion categorias variable Municipio
df['Municipio']= df['Municipio'].replace(['barbacoas','BARBACOAS'],'Barbacoas')
df['Municipio']= df['Municipio'].replace(['PIZARRO','FRANCISCO PIZARRO','pizarro'],'Pizarro')
df['Municipio']= df['Municipio'].replace(['MAGÜÍ - Payán','MAGUI PAYAN'],'Magui Payan')
df['Municipio']= df['Municipio'].replace(['TUMACO','tumaco'],'Tumaco')
df['Municipio']= df['Municipio'].replace(['UNIÓNPANAMERICANA','UNION PANAMERICANA'],'Unión Panamericana')
df['Municipio']= df['Municipio'].replace(['FLORIDA'],'Florida')
df['Municipio']= df['Municipio'].replace(['PUERTO SANTANDER','P/SNTDER','santander','puerto santander'],'Puerto Santander')
df['Municipio']= df['Municipio'].replace(['BUCARASICA'],'Bucarasica')
df['Municipio']= df['Municipio'].replace(['EL TARRA','el tarra'],'El Tarra')
df['Municipio']= df['Municipio'].replace(['SARDINATA'],'Sardinata')
df['Municipio']= df['Municipio'].replace(['tibu','TIBÚ'],'Tibú')
df['Municipio']= df['Municipio'].replace(['ABREGO','ÁBREGO'],'Ábrego')
df['Municipio']= df['Municipio'].replace(['CONVENCIÓN','CONVENCION'],'Convención')
df['Municipio']= df['Municipio'].replace(['EL CARMEN'],'El Carmen')
df['Municipio']= df['Municipio'].replace(['HACARÍ','hacari'],'Hacarí')
df['Municipio']= df['Municipio'].replace(['GUACARÍ','GUACARI'],'Guacarí')
df['Municipio']= df['Municipio'].replace(['SAN CALIXTO','san calixto'],'San Calixto')
df['Municipio']= df['Municipio'].replace(['TEORAMA'],'Teorama')
df['Municipio']= df['Municipio'].replace(['SANTIAGO-COLON','COLON PTYO'],'Santiago')
df['Municipio']= df['Municipio'].replace(['MOCOA','mocoa'],'Mocoa')
df['Municipio']= df['Municipio'].replace(['ORITO'],'Orito')
df['Municipio']= df['Municipio'].replace(['PUERTO ASIS'],'Puerto Asís')
df['Municipio']= df['Municipio'].replace(['PTO CAICEDO'],'Puerto Caicedo')
df['Municipio']= df['Municipio'].replace(['PUERTO GUZMAN'],'Puerto Guzmán')
df['Municipio']= df['Municipio'].replace(['SAN FRANCISCO-SIBUNDOY'],'San Francisco')
df['Municipio']= df['Municipio'].replace(['VALLE DEL GUAMUEZ-SAN MIGUEL'],'San Miguel')
df['Municipio']= df['Municipio'].replace(['VALLE DEL GUAMUEZ-SAN MIGUEL','VALLE DEL GUAMUEZ'],'Valle Del Guamuez')
df['Municipio']= df['Municipio'].replace(['VILLAGARZON','Villagarzon'],'Villagarzón')
df['Municipio']= df['Municipio'].replace(['circasia','CIRCASIA'],'Circasia')
df['Municipio']= df['Municipio'].replace(['FILANDIA'],'Filandia')
df['Municipio']= df['Municipio'].replace(['GENOVA'],'Genova')
df['Municipio']= df['Municipio'].replace(['MONTENEGRO','montenegro'],'Montenegro')
df['Municipio']= df['Municipio'].replace(['QUIMBAYA'],'Quimbaya')
df['Municipio']= df['Municipio'].replace(['la virginia'],'La Virginia')
df['Municipio']= df['Municipio'].replace(['marsella','MARSELLA'],'Marsella')
df['Municipio']= df['Municipio'].replace(['sibundoy','SIBUNDOY'],'Sibundoy')
df['Municipio']= df['Municipio'].replace(['CURITI','curiti'],'Curiti')
df['Municipio']= df['Municipio'].replace(['LOS SANTOS','Los santos','los Santos'],'Los Santos')
df['Municipio']= df['Municipio'].replace(['MOLAGAVITA'],'Molagavita')
df['Municipio']= df['Municipio'].replace(['OIBA','oiba'],'Oiba')
df['Municipio']= df['Municipio'].replace(['PALMAR','palmar'],'Palmar')
df['Municipio']= df['Municipio'].replace(['paramo','PARAMO'],'Paramo')
df['Municipio']= df['Municipio'].replace(['SABANA DE TORRES'],'Sabana de torres')
df['Municipio']= df['Municipio'].replace(['San gil','SAN GIL'],'San Gil')
df['Municipio']= df['Municipio'].replace(['San Jose de Suaita','SUAITA'],'Suaita')
df['Municipio']= df['Municipio'].replace(['chalan','CHALAN'],'Chalan')
df['Municipio']= df['Municipio'].replace(['MORROA'],'Morroa')
df['Municipio']= df['Municipio'].replace(['OVEJAS','ovejas'],'Ovejas')
df['Municipio']= df['Municipio'].replace(['coveñas','COVEÑAS'],'Coveñas')
df['Municipio']= df['Municipio'].replace(['San antonio de palmito','San Antonio de palmito','San Antonio de Palmito','PALMITO'],'Palmito')
df['Municipio']= df['Municipio'].replace(['ONOFRE'],'San Onofre')
df['Municipio']= df['Municipio'].replace(['TOLUVIEJO','toluviejo'],'Toluviejo')
df['Municipio']= df['Municipio'].replace(['COROZAL','corozal'],'Corozal')
df['Municipio']= df['Municipio'].replace(['LOS PALMITOS'],'Los Palmitos')
df['Municipio']= df['Municipio'].replace(['Sincé'],'Since')
df['Municipio']= df['Municipio'].replace(['HERVEO'],'Herveo')
df['Municipio']= df['Municipio'].replace(['SANTA ISABEL'],'Santa Isabel')
df['Municipio']= df['Municipio'].replace(['ataco','ATACO'],'Ataco')
df['Municipio']= df['Municipio'].replace(['chaparral','CHAPARRAL'],'Chaparral')
df['Municipio']= df['Municipio'].replace(['ALCALÁ','alcala','ALCALA'],'Alcalá')
df['Municipio']= df['Municipio'].replace(['BUENAVENTURA','buenaventura'],'Buenaventura')
df['Municipio']= df['Municipio'].replace(['CAICEDONIA'],'Caicedonia')
df['Municipio']= df['Municipio'].replace(['CANDELARIA'],'Candelaria')
df['Municipio']= df['Municipio'].replace(['ANTIOQUIA'],'Antioquia')
df['Municipio']= df['Municipio'].replace(['GINEBRA','ginebra'],'Ginebra')
df['Municipio']= df['Municipio'].replace(['VERSALLES'],'Versalles')
df['Municipio']= df['Municipio'].replace(['CARURU','caruru'],'Caruru')
df['Municipio']= df['Municipio'].replace(['MITU'],'Mitú')
df['Municipio']= df['Municipio'].replace(['TARAIRA'],'Taraira')
df['Municipio']= df['Municipio'].replace(['CUMARIBO'],'Cumaribo')
df['Municipio']= df['Municipio'].replace(['La primavera'],'La Primavera')
df['Municipio']= df['Municipio'].replace(['PUERTO CARREÑO'],'Puerto Carreño')
df['Municipio']= df['Municipio'].replace(['SANTA ROSALIA'],'Santa Rosalía')
df['Municipio']= df['Municipio'].replace(['SAN ANTONIO DE PADUA'],'VIGIA DEL FUERTE')
df['Municipio']= df['Municipio'].replace(['CHOCO'],'Choco')
df['Municipio']= df['Municipio'].replace(['la meta'],'meta')
df['Municipio']= df['Municipio'].replace(['BARRIO MARIA ANTONIA'],'NECOCLI')
df['Municipio']= df['Municipio'].replace(['BOLÍVAR'],'Bolivar')
df['Municipio']= df['Municipio'].replace(['S.J URE'],'San Jose De Ure')

#Homologación categorías de la variable Deporte 1
df['Deporte 1'] = df['Deporte 1'].replace(['BÉISBOL','BEISBOL'], 'Beisbol')
df['Deporte 1'] = df['Deporte 1'].replace(['FÚTBOL DE SALÓN','FÚTBOL SALA','Fútbol de salon','Fútbol de salón','FUTBOL DE SALON','Futbol de Salon', 'fútbol de salón','futbol de salon','FÚTBOL SE SALÓN','Futbol de salón','FÚTBOL SALÓN','FUTBOL SALON','FUTBOL DE SALÓN','FÙTBOL DE SALÒN'], 'Fútbol de Salón')
df['Deporte 1'] = df['Deporte 1'].replace(['FUTBOL','FÚTBOL','Futbol','futbol','Fulbol'], 'Fútbol')
df['Deporte 1'] = df['Deporte 1'].replace(['PATINAJE','patinaje'], 'Patinaje')
df['Deporte 1'] = df['Deporte 1'].replace(['BOXEO'], 'Boxeo')
df['Deporte 1'] = df['Deporte 1'].replace(['VOLEIBOL','Voleibol piso'],'Voleibol')
df['Deporte 1'] = df['Deporte 1'].replace(['ATLETISMO'], 'Atletismo')  
df['Deporte 1'] = df['Deporte 1'].replace(['BALONCESTO', 'baloncesto'],'Baloncesto')
df['Deporte 1'] = df['Deporte 1'].replace(['AJEDREZ'],'Ajedrez')    
df['Deporte 1'] = df['Deporte 1'].replace(['RUGBY'],'Rugby')
df['Deporte 1'] = df['Deporte 1'].replace(['TAEKWONDO', 'taekwondo'], 'Taekwondo')
df['Deporte 1'] = df['Deporte 1'].replace(['KARATE DO', 'KARATE'],'Karate')
df['Deporte 1'] = df['Deporte 1'].replace(['JUDO', 'judo'], 'Judo')
df['Deporte 1'] = df['Deporte 1'].replace(['TIRO CON ARCO', 'Tiro Arco'], 'Tiro con arco')
df['Deporte 1'] = df['Deporte 1'].replace(['LUCHA', 'lucha'],'Lucha')
df['Deporte 1'] = df['Deporte 1'].replace(['BALONMANO', 'Balon mano'], 'Balonmano')
df['Deporte 1'] = df['Deporte 1'].replace(['NATACIÓN', 'NATACION', 'NATACIOON'],'Natación')
df['Deporte 1']= df['Deporte 1'].replace(['CICLISMO'], 'Ciclismo')
df['Deporte 1']= df['Deporte 1'].replace(['LEVANTAMIENTO DE PESAS'],'Levantamiento de pesas' )
df['Deporte 1']= df['Deporte 1'].replace(['CANOTAJE'],'Canotaje')
df['Deporte 1']= df['Deporte 1'].replace(['SURF'],'Surf')
df['Deporte 1']= df['Deporte 1'].replace(['balonpesado'],'Balonpesado')

#---------------------------------------------------------------------------------
#Renombrar columna 'Mes\ninscripción'
df = df.rename(columns ={'Mes\ninscripción':'Mes inscripción'}) 

df2 = df.copy()
pd.options.display.float_format = '{:.0f}'.format # organizar los decimales
df2 = df2.dropna()
#se reemplazan los años
df2['Año inscripción'] = df2['Año inscripción'].replace({2021.000: '2021',2020.000:'2020', 2.019:'2019'})
df2['Día inscripción'] = df2['Día inscripción'].astype(int)
df2['Mes inscripción']= df2['Mes inscripción'].astype(int)
df2['Año inscripción']= df2['Año inscripción'].astype(int)

#se eliminan algunos datos con condiciones
df2 = df2.drop(df2[df2['Día inscripción']<=1].index)
df2 = df2.drop(df2[df2['Día inscripción']>=31].index)

#Ahora concatenamos las variables año, mes y día en una sola variable
fechacomplet = df2['Año inscripción'].astype(str) + "-" + df2['Mes inscripción'].astype(str) + "-" + df2['Día inscripción'].astype(str)
# Ahora convertimos los datos en tipo fecha
df2['Fecha']= pd.to_datetime(fechacomplet)

#---------------------------------------------------------------------------------
c1, c2= st.columns((1,1))


#---------------------------------------------------------------------------------
c1.markdown("<h3 style='text-align: center; color: gray;'>INSCRIPCIÓN POR AÑO</h3>", unsafe_allow_html=True)
#SERIE DE TIEMPO
serie = df2.groupby(['Fecha'])[['Deporte 1']].count().reset_index()
print(serie)
seriegp = serie.copy()
seriegp.reset_index()
seriegp.iloc[:,1:] = seriegp.rolling(window=7).mean().fillna(0)
fig = px.line(seriegp, x='Fecha', y='Deporte 1')

# agregar detalles
fig.update_layout(
    xaxis_title = 'Años',
    yaxis_title = 'Inscripciones',
    template = 'simple_white',
    title_x = 0.5,
    showlegend=False,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)', 
    width=600, height=400)
fig.update_traces(line_color='red')
# Enviar gráfica a streamlit
c1.plotly_chart(fig)

#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------
#Se agrupa por departamento
graf2=df2.groupby(["Departamento"])[["Edad"]].count().reset_index().rename(columns={'Edad':'Total deportistas'}).sort_values('Total deportistas', ascending = False).head(10)


c2.markdown("<h3 style='text-align: center; color: gray;'>EDAD Y DEPARTAMENTO</h3>", unsafe_allow_html=True)
# crear gráfica
fig1 = px.bar(graf2, x='Departamento', y='Total deportistas', color = 'Departamento',color_discrete_map={'Antioquia':'lime','Chocó':'darkgreen','Bolívar':'yellow','Sucre':'white','Atlántico':'red','Córdoba':'mediumblue','Nariño':'gold','Cesar':'lawngreen','Tolima':'darkred','Cauca':'forestgreen'})

# agregar detalles a la gráfica
fig1.update_layout(
    xaxis_title = 'Departamento',
    yaxis_title = 'Total Deportistas',
    template = 'simple_white',
    title_x = 0.5,
    legend_title = '<b>Departamento<b>',
    showlegend=False,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)', 
    width=600, height=400)

c2.plotly_chart(fig1)


#---------------------------------------------------------------------------------
df2['longitude'] = df2.apply(lambda x: -75.834573 if (x['Departamento']=='Córdoba')else -69.126672 if (x['Departamento']=='Guainía')else -75.945171 if (x['Departamento']=='Putumayo')else -70.747624 if (x['Departamento']=='Vaupés')else -72.631597 if (x['Departamento']=='La Guajira')else -73.087882 if (x['Departamento']=='Boyacá')else -72.839239 if (x['Departamento']=='Norte de Santander')else -75.518214 if (x['Departamento']=='Antioquia')
else -76.858550 if (x['Departamento']=='Cauca')else -76.956470 if (x['Departamento']=='Chocó')else -71.083844 if (x['Departamento']=='Arauca')else -77.358327 if (x['Departamento']=='Nariño')else -75.248607 if (x['Departamento']=='Tolima')else -72.244439 if (x['Departamento']=='Guaviare')else -71.593744 if (x['Departamento']=='Casanare')else -74.955709 if (x['Departamento']=='Atlántico')else -74.312098 if (x['Departamento']=='Bolívar')
else -75.094428 if (x['Departamento']=='Sucre')else -71.567136 if (x['Departamento']=='Amazonas')else -73.487266 if (x['Departamento']=='Santander')else -76.553070 if (x['Departamento']=='Valle del Cauca')else -75.353790 if (x['Departamento']=='Caldas')else -69.332739 if (x['Departamento']=='Vichada')else -75.694243 if (x['Departamento']=='Huila')else -74.383413 if (x['Departamento']=='Magdalena')else -74.081474 if (x['Departamento']=='Cundinamarca')
else -75.701540 if (x['Departamento']=='Quindío')else -75.914475 if (x['Departamento']=='Risaralda')else -72.985110 if (x['Departamento']=='Meta')else -74.224387 if (x['Departamento']=='Caquetá')else -73.656878 if (x['Departamento']=='Cesar')else -81.720393 if (x['Departamento']=='San Andrés')else x['Departamento'], axis = 1)

df2['latitude'] = df2.apply(lambda x: 8.457079 if (x['Departamento']=='Córdoba')else 2.795118 if (x['Departamento']=='Guainía')else 0.574873 if (x['Departamento']=='Putumayo')else 0.847465 if (x['Departamento']=='Vaupés')else 11.404261 if (x['Departamento']=='La Guajira')else 5.586472 if (x['Departamento']=='Boyacá')else 8.074825 if (x['Departamento']=='Norte de Santander')else 6.720107 if (x['Departamento']=='Antioquia')
else 2.457311 if (x['Departamento']=='Cauca')else 5.934771 if (x['Departamento']=='Chocó')else 6.615828 if (x['Departamento']=='Arauca')else 1.289806 if (x['Departamento']=='Nariño')else 4.038548 if (x['Departamento']=='Tolima')else 1.922696 if (x['Departamento']=='Guaviare')else 5.390435 if (x['Departamento']=='Casanare')else 10.705318 if (x['Departamento']=='Atlántico')else 8.840400 if (x['Departamento']=='Bolívar')
else 9.139637 if (x['Departamento']=='Sucre')else -1.277734 if (x['Departamento']=='Amazonas')else 6.752032 if (x['Departamento']=='Santander')else 3.758128 if (x['Departamento']=='Valle del Cauca')else 5.273203 if (x['Departamento']=='Caldas')else 4.876782 if (x['Departamento']=='Vichada')else 2.430359 if (x['Departamento']=='Huila')else 10.242332 if (x['Departamento']=='Magdalena')else 5.016929 if (x['Departamento']=='Cundinamarca')
else 4.457892 if (x['Departamento']=='Quindío')else 4.924370 if (x['Departamento']=='Risaralda')else 3.469446 if (x['Departamento']=='Meta')else 0.788243 if (x['Departamento']=='Caquetá')else 9.270039 if (x['Departamento']=='Cesar')else 12.544136 if (x['Departamento']=='San Andrés')else x['Departamento'], axis = 1)
#---------------------------------------------------------------------------------
st.markdown("<h3 style='text-align: center; color: gray;'>¿CUÁNTAS PERSONAS SE INSCRIBEN POR DEPARTAMENTO CADA AÑO?</h3>", unsafe_allow_html=True)

año = st.slider('Año de inscripción', 2019, 2021) # Crear variable que me almacene la hora seleccionada
df3 = df2[df2['Año inscripción']==año] # Filtrar DataFrame

st.write(pdk.Deck( # Código para crear el mapa
    
    # Set up del mapa
    map_style='mapbox://styles/mapbox/dark-v10',
    initial_view_state={
        'latitude' : 4.368564,
        'longitude': -73.908284, 
        'zoom' : 5,
        'pitch': 40
        },
    
    # Capa con información
    layers = [pdk.Layer(
        'HexagonLayer',
        data = df2[['latitude','longitude']],
        get_position = ['longitude','latitude'],
        radius = 30000,
        extruded = True,
        elevation_scale = 10,
        elevation_range = [0,10000])]))

