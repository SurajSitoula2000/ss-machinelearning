import streamlit as st
import pandas as pd
import numpy as np

st.title('🐱‍💻 Machine Learning App')

st.info('This is app builds a machine learning model!')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/SurajSitoula2000/ss-machinelearning/refs/heads/master/penguins_size.csv')
  df

  st.write('**X**')
  X = df.drop('species', axis=1)
  X

  st.write('**y**')
  y = df.species
  y

with st.expander('Data Visualization'):
  st.scatter_chart(data=df, x='culmen_length_mm', y='body_mass_g', color='species')

# Data preparation
with st.sidebar:
  st.header('Input features')
  island = st.selectbox('Island', ('Torgersen', 'Biscoe', 'Dream'))
  culmen_length_mm = st.slider('Culmen length (mm)', 32.1, 59.6, 41.9)
  culmen_dipper_mm = st.slider('Culmen dipper (mm)', 13.1, 21.5, 17.2)
  flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body mass (m)', 2700.0, 6300.0, 4207.0)
  gender = st.selectbox('Gender', ('male', 'female'))

  # Create a DataFrame for the input features
  data = {'island': island,
          'culmen_length_mm': culmen_length_mm,
          'culmen_dipper_mm ': culmen_dipper_mm,
          'flipper_length_mm': flipper_length_mm,
          'body_mass_g': body_mass_g,
          'gender': gender}
  input_df = pd.DataFrame(data, index=[0])
  input_penguins = pd.concat([input_df, X], axis=0)

with st.expander('Input features'):
  st.write('**Input penguins**')
  input_df
  st.write('**Combines penguins data**')
  input_penguins

