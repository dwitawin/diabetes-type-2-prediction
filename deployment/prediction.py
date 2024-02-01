import pandas as pd
import streamlit as st
import numpy as np
import pickle
import json

# Load All Files

with open('model.pkl', 'rb') as file_1:
  model = pickle.load(file_1)

def run():
    st.write('# Diabetes Risk Prediction')
    with st.form('form_diabetes'):
        age = st.number_input('Age', min_value=5, max_value=99, value=18, step=1)
        weight = st.number_input('Weight', min_value=60, max_value=150, value=70, help='in Kilograms')
        height = st.slider('Height',100,250,170, help='in Centimeters')
        bmi = st.number_input('BMI', min_value=1, max_value=9999, value=50)
        sex = st.selectbox('Gender', [1,2], help='male,female')
        marital = st.selectbox('Marital Status', ['Married','Divorced','Widowed', 'Separated', 'Never Married', 'A member of an unmarried couple', 'Refused to Answer'])
        educa = st.selectbox('Education', ['Never attended school or only kindergarten','Elementary','Some high school', 'High school graduate', 'Some college or technical school', 'College graduate', 'Refused to Answer'])
        st.markdown('---')

        income = st.selectbox('Income', ['Less than $10,000','$10,000 to less than $15,000','$15,000 to less than $20,000', '$20,000 to less than $25,000', '$25,000 to less than $35,000', '$35,000 to less than $50,000', '$50,000 to less than $75,000', '$75,000 or more', 'Don’t know/Not sure','Refused to Answer'])
        pregnant = st.selectbox('Pregnant', ['Yes', 'No', 'Dont Know/Not Sure', 'Refused to Answer'])
        smoke = st.selectbox('Smoke', ['Yes', 'No', 'Dont Know/Not Sure', 'Refused to Answer'])
        drink = st.selectbox('Drink', ['Yes', 'No', 'Refused to Answer'])
        fruit = st.selectbox('Fruit', ['Yes', 'No', 'Refused to Answer'])
        vege = st.selectbox('Vegetable', ['Yes', 'No', 'Refused to Answer'])
        exercise = st.selectbox('Exercise', ['Yes', 'No', 'Refused to Answer'])
        st.markdown('---')

        genhlth = st.selectbox('General Health', ['Yes', 'No', 'Refused to Answer'])
        phyhlth = st.selectbox('Physical Health', ['Yes', 'No', 'Refused to Answer'])
        menthhlth = st.selectbox('Mental Health', ['Yes', 'No', 'Refused to Answer'])
        checkup1 = st.selectbox('Check UP', ['Yes', 'No', 'Refused to Answer'])
        hlthpln1 = st.selectbox('Health Plan', ['Yes', 'No', 'Refused to Answer'])
        decide = st.selectbox('Decision Ability', ['Yes', 'No', 'Refused to Answer'])
        hbpres = st.selectbox('High Blood Pressure', ['Yes', 'No', 'Refused to Answer'])
        bchol = st.selectbox('Blood Cholestrol', ['Yes', 'No', 'Refused to Answer'])
        st.markdown('---')

        submitted = st.form_submit_button('Predict')

        num_sex = ()

    data_inf = {
        'GENHLTH':genhlth, 
        'PHYSHLTH':phyhlth, 
        'MENTHLTH':menthhlth, 
        'CHECKUP1':checkup1, 
        'HLTHPLN1':hlthpln1, 
        'SEX': sex,
        '_AGE65YR':age, 
        'MARITAL':marital, 
        'EDUCA':educa, 
        'INCOME2':income, 
        'WTKG3':weight, 
        'HTM4':height, 
        '_BMI5':bmi,
        'PREGNANT':pregnant, 
        'DECIDE':decide, 
        '_RFHYPE5':hbpres, 
        'TOLDHI2':bchol, 
        '_RFSMOK3':smoke, 
        '_RFDRHV5':drink,
        '_FRTLT1':fruit, 
        '_VEGLT1':vege, 
        '_TOTINDA':exercise
    }
    data_inf = pd.DataFrame([data_inf])

    if submitted:
        # convert value in variable sex


        #predict using Linear Regression
        y_pred_inf = model.predict(data_inf)
        st.write('# Resiko Diabetes:', str(int(y_pred_inf)))

if __name__ == '__main__':
    run()