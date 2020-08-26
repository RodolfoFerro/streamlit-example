from sklearn.datasets import load_iris
import streamlit as st
import pandas as pd
import numpy as np


from iris import iris_classifier
from figure import plotly_figure_1
from figure import plotly_figure_2


data = load_iris()
iris = pd.DataFrame(data.data, columns=data.feature_names)
classes = data.target_names

models = {
    "Árbol de decisión": iris_classifier()
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
st.dataframe(iris)

# Sección de datos
st.write(
    """
    Y un pequeño gráfico generado con Plotly.
    """
)
fig = plotly_figure_2(iris)
st.plotly_chart(fig)

# Selección del modelo
model_selector = st.sidebar.selectbox(
    "Selecciona el modelo a utilizar:",
    list(models.keys())
)
model = models[model_selector]

# Especificación de datos
st.write(
    """
    Especificamos las características:
    """
)
sepal_lenght = st.slider(
    "Longitud del sépalo", 0.0, 10.0, 5.0, 0.05
)
sepal_width = st.slider(
    "Ancho del sépalo", 0.0, 5.0, 2.5, 0.05
)
petal_lenght = st.slider(
    "Longitud del pétalo", 0.0, 8.0, 4.0, 0.05
)
petal_width = st.slider(
    "Ancho del pétalo", 0.0, 3.0, 1.5, 0.05
)

# Predicción
features = np.array([[sepal_lenght, sepal_width, petal_lenght, petal_width]])
prediction = model.predict(features)[0]

st.write(
    """
    De acuerdo a la predicción del modelo, la clase correspondiente es: 
    """
)
st.header(f'{classes[prediction]}')