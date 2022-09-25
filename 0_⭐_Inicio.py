# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 15:08:21 2022

@author: Dell
"""
# Contents of ~/my_app/streamlit_app.py
import streamlit as st
st.set_page_config(
    page_title='multipaginas app',
    page_icon='👽'
    )
st.markdown("<h1 style = 'text-align:center;color:red;'>🏆 DEPORTES EN COLOMBIA🥇🏅</h1>", unsafe_allow_html=True)

st.sidebar.success('SELECCIONE UNA PAGÍNA')

from PIL import Image
image = Image.open('deportes.jpg')
st.image(image, caption='DEP')
st.markdown("")
st.markdown("<h5 style = 'text-align:center;color:gray;'><b>El deporte es de suma importancia, ya que genera bienestar, tiene tanto beneficios fisicos, mentales y sociales, por esto es de gran importancia fomentar las practicas deportivas. El deporte es una herramienta de transformacion social y una actividad formadora, ya que desarrolla un papel como promotor de integracion social y desarrollo economico, en diferentes contextos geograficos, culturales y politicos.' </h5>", unsafe_allow_html=True)
st.markdown("<h4 style = 'text-align:center;color:gray;'><b>Elaborado por:<b> Sebastian Alzate, Luis Mejia, Sara Delgado y Juan Sebastian Jaramillo </h4>", unsafe_allow_html=True)
