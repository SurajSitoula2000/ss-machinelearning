import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.title('🐱‍💻 Machine Learning App')

st.info('This is app builds a machine learning model!')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/SurajSitoula2000/ss-machinelearning/refs/heads/master/penguins_size.csv')
  df

  st.write('**X**')
  X_raw = df.drop('species', axis=1)
  X_raw

  st.write('**y**')
  y_raw = df.species
  y_raw

with st.expander('Data Visualization'):
  st.scatter_chart(data=df, x='culmen_length_mm', y='body_mass_g', color='species')

# Input features
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
          'sex': gender}
  input_df = pd.DataFrame(data, index=[0])
  input_penguins = pd.concat([input_df, X_raw], axis=0)

with st.expander('Input features'):
  st.write('**Input penguins**')
  input_df
  st.write('**Combines penguins data**')
  input_penguins

# Data preparation
# Encode x
encode = ['island', 'sex']
df_penguins = pd.get_dummies(input_penguins, prefix=encode)

X = df_penguins[1:]
input_row = df_penguins[:1]

# Encode y
target_mapper = {'Adelie':0,
                 'Chinstrap':1,
                 'Gentoo':2}
def target_encode(val):
  return target_mapper[val]

y = y_raw.apply(target_encode)

with st.expander('Data preparation'):
  st.write('**Encoded X (input penguin)**')
  input_row
  st.write('**Encoded y**')
  y

# Model training and inference
## Train the ML Model
clf = RandomForestClassifier()
clf.fit(X, y)

## Apply model to make prediction
prediction = clf.predict(input_row)
prediction_proba = clf.predict_proba(input_row)

df_prediction_proba = pd.DataFrame(prediction_proba)
df_prediction_proba.columns = ['Adelie', 'Chinstrap', 'Gentoo']
df_prediction_proba = df_prediction_proba.rename(columns={0: 'Adelie',
                                    1: 'Chinstrap',
                                    2: 'Gentoo'})

# Display predicted species
st.subheader('Predicted Species')
st.dataframe(df_prediction_proba,
             column_config={
              'Adelie':st.column_config.ProgressColumn(
                'Adelie',
                format='%f',
                width='medium',
                min_value=0,
                max_value=1
            ),
              'Chinstrap':st.column_config.ProgressColumn(
                'Chinstrap',
                format='%f',
                width='medium',
                min_value=0,
                max_value=1
          ),
              'Gentoo':st.column_config.ProgressColumn(
                'Gentoo',
                format='%f',
                width='medium',
                min_value=0,
                max_value=1
            ),
          }, hide_index=True)
      
                
penguins_species = np.array(['Adelie', 'Chinstrap', 'Gentoo'])
st.success(str(penguins_species[prediction][0]))



