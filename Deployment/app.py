import streamlit as st
import eda
import prediction

# page
page = st.sidebar.selectbox('Pilih Halaman',('Exploratory Data Analysis (EDA)','Prediction'))

if page == 'Exploratory Data Analysis (EDA)':
    eda.run()
else:
    prediction.run()
    