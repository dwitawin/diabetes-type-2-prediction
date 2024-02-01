import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(
    page_title = 'Exploratory Data Behavioural - Diabetes',
    layout = 'wide',
    initial_sidebar_state = 'expanded'
)

def run():
    # membuat header
    st.write('# Behavioural Data Diabetes')

    # membuat subheader
    st.write('# Exploratory Data Analysis')

    # add markdown
    st.markdown('---')

    # add dataset pandas 
    st.write('### Behavioural Data Diabetes Display')
    data = pd.read_csv('P1M2_dwita.csv')

    # add markdown
    st.markdown('---')

    # data viz: by age
    st.write('#### Distribusi Usia Kelompok 18-64 tahun')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x=data['_AGE65YR'], palette='hsv')
    st.pyplot(fig)

    # data viz: scatterplot by karakteristik
    st.write('#### Scatterplot Karakteristik')
    fig = plt.figure(figsize=(15,5))
    plt.subplot(1, 3, 1)
    sns.scatterplot(x='HTM4', y='DIABETE3', data=data)
    plt.title('Height vs Diabetes')

    plt.subplot(1, 3, 2)
    sns.scatterplot(x='WTKG3', y='DIABETE3', data=data)
    plt.title('Weight vs Diabetes')

    plt.subplot(1, 3, 3)
    sns.scatterplot(x='_BMI5', y='DIABETE3', data=data)
    plt.title('BMI vs Diabetes')
    st.pyplot(fig)

    # data viz: by age
    df_diabetes = data.query('DIABETE3 == 1 or DIABETE3 == 2')
    labels = ['Female', 'Male']
    size = df_diabetes['SEX'].value_counts()
    colors = ['blue','red']
    explode = [0.1, 0]

    fig, axes = plt.subplots(figsize=(7,5))
    plt.pie(size, colors=colors, explode=explode, labels=labels, shadow=True, startangle=90, autopct='%.2f%%')
    plt.title('Diabetes Percentage by Gender', fontsize=15)
    plt.legend()

    # add markdown
    st.markdown('---')

    # end
    st.write('#### Tugas M2 - FTDS RMT 24')
    st.write('#### Page dibuat oleh Dwita Alya')


if __name__ == '__main__':
    run()