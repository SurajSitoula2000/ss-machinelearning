import streamlit as st
import pandas as pd
import numpy as pd

st.title('🐱‍💻 Machine Learning App')

st.info('This is app builds a machine learning model!')

df = pd.read_csv(r"https:\\github.com\SurajSitoula2000\ss-machinelearning\blob\master\penguins_size.csv")
df

