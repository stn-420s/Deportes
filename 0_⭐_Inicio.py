# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 15:08:21 2022

@author: Dell
"""
# Contents of ~/my_app/streamlit_app.py
import streamlit as st
st.set_page_config(
    page_title='DEPORTES COLOMBIA',
    page_icon='👽'
    )
st.markdown("<h1 style = 'text-align:center;color:red;'>🏆 DEPORTES EN COLOMBIA🥇🏅</h1>", unsafe_allow_html=True)

st.sidebar.success('NO PAIN NO GAIN')

from PIL import Image

image2= Image.open('dep.jpg')

st.image(image2)    
st.markdown("")
st.markdown("<h5 style = 'text-align:center;color:gray;'><b>El deporte es de suma importancia en el desarrollo de las poblaciones debido a que proporciona beneficios físicos, mentales y sociales, por lo que incentivar estas prácticas debe de ser una prioridad. El deporte es una herramienta de transformación social y una actividad formadora que desarrolla un papel de integración social y desarrollo económico en diferentes contextos  como lo son geográficos, culturales y políticos.</h5>", unsafe_allow_html=True)
st.markdown("<h4 style = 'text-align:center;color:gray;'><b>Elaborado por:<b> Sebastian Alzate, Luis Mejia, Sara Delgado y Juan Sebastian Jaramillo </h4>", unsafe_allow_html=True)