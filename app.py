# ==============================================================
# Author: Rodolfo Ferro
# Twitter: @rodo_ferro
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script has been originally created by Rodolfo Ferro.
# Any explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ==============================================================
# 
# Contexto:
#
# * Tenemos una función que entrena un modelos de 
#   clasificación sobre los datos de iris. Dicha función
#   la encuentras en iris.py (ahí puedes agreagar otros
#   modelos).
# * Tenemos funciones para visualizar datos. Las funciones 
#   fueron hechas con Plotly y las encuentras en figure.py.
# 
# ==============================================================
# 
# Tareas:
#
# Rellenar los espacios con la etiqueta TODO. Básicamente 
# es realizar lo que se indica en los siguientes puntos. 
# 
# 1. Desplegar el dataframe de los datos.
# 2. Desplegar una figura con los datos.
# 3. Crear barra lateral con selector de modelo.
# 4. Crear sliders para datos de entrada.
# 5. Realizar predicción y desplegar resultado.
#
# ==============================================================

# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris
import streamlit as st
import pandas as pd
import numpy as np

from iris import decision_tree
from figure import plotly_figure_1
from figure import plotly_figure_2


data = load_iris()
iris = pd.DataFrame(data.data, columns=data.feature_names)
classes = data.target_names

models = {
    "Árbol de decisión": decision_tree()
}


# Sección de introducción
st.title("Predicción de especies de Iris usando scikit-learn y Streamlit")
st.write(
    """
    Bienvenid@ a este sencillo ejemplo que ejecuta un modelo entrenado 
    de scikit-learn directo en Streamlit. 
    """
)

# Sección de datos
st.write(
    """
    A continuación los datos utilizados.
    """
)
# TODO: 
# st.dataframe(dataframe)

# Sección de datos
st.write(
    """
    Y un pequeño gráfico generado con Plotly.
    """
)
# TODO: 
# figure = create_figure(iris)
# st.plotly_chart(figure)

# Selección del modelo
# TODO: 
# model_selector = st.sidebar.selectbox(title, list)
# Use list form models.keys()
# Then make model = models[model_selector] to get the specified model

# Especificación de datos
st.write(
    """
    Especificamos las características:
    """
)

# TODO:
# Create a st.slider(text, min, max, start, step) for
# each feature in iris.columns:
# sepal_length (cm) -> (0.0, 10.0, 5.0, 0.05)
# sepal_width (cm) -> (0.0, 5.0, 2.5, 0.05)
# petal_length (cm) -> (0.0, 8.0, 4.0, 0.05)
# petal_width (cm) -> (0.0, 3.0, 1.5, 0.05)

# Predicción
# TODO: 
# features = np.array([[sepal_lenght, sepal_width, petal_lenght, petal_width]])
# prediction = model.predict(features)[0]
# tag = classes[prediction]
tag = None

st.markdown(
    f"""
    De acuerdo a la predicción del modelo, la clase correspondiente es: 

    ### {tag}
    """
)
