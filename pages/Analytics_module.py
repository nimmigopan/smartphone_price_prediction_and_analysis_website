import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(page_title="viz Demo")

st.title('Overall Analysis')

df = pd.read_csv('final_data_for_modelling.csv')
#st.dataframe(df)


col1, col2 = st.columns(2)
with col1:
    st.subheader('price range for different brands')
    sns.barplot(data=df,x='brand_name',y='price')
    plt.xticks(rotation='vertical')
    st.pyplot()
with col2:
    st.subheader('price range for different processor brands')
    sns.barplot(data=df, x='processor_brand', y='price')
    st.pyplot()

col1, col2 = st.columns(2)
with col1:
    st.subheader('price range for RAM')
    sns.barplot(data=df,x='ram',y='price')
    st.pyplot()
with col2:
    st.subheader('price range for ROM')
    sns.barplot(data=df,x='rom',y='price')
    st.pyplot()

col1, col2 = st.columns(2)
with col1:
    st.subheader('price range for Refresh rates')
    sns.barplot(data=df,x='refresh_rate',y='price')
    st.pyplot()
with col2:
    st.subheader('price range for screen resolution')
    sns.barplot(data=df,x='resolution',y='price')
    st.pyplot()

st.subheader('Speed of Processor vs Price')
sns.scatterplot(data=df,x='processor_speed',y='price')
st.pyplot()