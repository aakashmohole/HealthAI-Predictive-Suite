import streamlit as st
import pickle
import pandas as pd

# model = open("Models/heart_desies_rfmodel.pkl", "rb") 
# classifier  = pickle.load(model)

def main():
    ## Tabes 
    Prediction, Data_info, Visualization = st.tabs(["Prediction", "Dataset Overview", "Visualization"])
    with Prediction:
        c1, c2 = st.columns(2)
        c3, c4 = st.columns(2)
        c5, c6 = st.columns(2)
        c7, c8 = st.columns(2)
        c9, c10 = st.columns(2)
        c11, c12 = st.columns(2)
        c13, c14 = st.columns(2)
        c15, c16 = st.columns(2)

        
        with c1:
                age = st.text_input("Age of person",value=0)
        with c2:
            gender_option = st.selectbox(
                'Select Gender',
                ('Male', 'Female'))
            if gender_option == 'Male':
                gender = 1    
            else:
                gender = 0
            
        with c3:
            cp_option = st.selectbox(
                'Select Chest pain type',
                ('Typical angina', 'Atypical angina', 'Non-anginal pain', 'Asymptomatic'))
            if cp_option == 'Typical angina':
                cp = 0  
            elif cp_option == 'Atypical angina':
                cp = 1
            elif cp_option == 'Non-anginal pain':
                cp = 2
            else: cp = 3
            
        with c4:
            trestbps = st.number_input('Enter Resting blood pressure (in mm Hg on admission to the hospital)')

        with c5:
            chol = st.number_input("Enter Serum cholestoral in mg/dl")
        with c6:
            fbs_option = st.selectbox(
                'Is fasting blood sugar > 120 mg/dl ?',
                ('True', 'False'))
            if fbs_option == 'True':
                fbs = 0      
            else:
                fbs = 1
            
        with c7:
            restecg_option = st.selectbox(
                'Select resting electrocardiographic results: ',
                ('Normal', 'Having ST-T wave abnormality', 'Showing probable or definite left ventricular hypertrophy by Estes criteria'))
            if restecg_option == 'Normal':
                restecg = 0  
            elif restecg_option == 'Having ST-T wave abnormality':
                restecg = 1
            else: restecg = 2
            
        with c8:
            thalach = st.number_input('Maximum heart rate achieved')
        
        with c9:
            exang_option = st.selectbox(
                'Exercise induced angina ',
                ('Yes', 'No'))
            if exang_option == 'No':
                fruits = 0  
            else:
                fruits = 1
        
        with c10:
            oldpeak = st.number_input('ST depression induced by exercise relative to rest', value=2.3)
        with c11:
            slope_option = st.selectbox(
                'The slope of the peak exercise ST segment ',
                ('Upsloping', 'Flat', 'Downsloping'))
            if slope_option == 'Upsloping':
                slope	 = 0  
            elif slope_option == 'Flat':
                slope	 = 1
            else : slope = 2
            
        with c12 :
            ca = st.number_input('Number of major vessels (0-3) colored by flourosopy')
            

        with c13:
            thal_option = st.selectbox(
                'Select Thal?',
                ('Error (in the original dataset 0 maps to NaN', 'Fixed defect','Normal', 'Reversable defect'))
            if thal_option == 'Error (in the original dataset 0 maps to NaN':
                thal = 0  
            elif thal_option == 'Fixed defect':
                thal = 1
            elif thal_option == 'Normal':
                thal = 2
            else: thal =3

    
if __name__ == '__main__':
    main()