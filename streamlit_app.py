import streamlit as st
import pandas as pd
import numpy as np

st.title('🐱‍💻 Machine Learning App')

st.info('This is app builds a machine learning model!')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/SurajSitoula2000/ss-machinelearning/refs/heads/master/penguins_size.csv')
  df
