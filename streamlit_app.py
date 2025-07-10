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
# island,culmen_length_mm,culmen_depth_mm,flipper_length_mm,body_mass_g,sex
  island = st.selectbox('Island', ('Torgersen', 'Biscoe', 'Dream'))
  gender = st.selectbox('Gender', ('male', 'female'))
  culmen_length_mm = st.slider('Culmen length (mm)', 32.1, 59.6, 41.9)
  
  

















