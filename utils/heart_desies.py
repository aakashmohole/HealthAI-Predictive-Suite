import streamlit as st
import pickle
import pandas as pd

model = open("Models/heart_desies_rfmodel.pkl", "rb") 
classifier  = pickle.load(model)

def perdicton_func(age, gender, cp, trestbps,chol, fbs, restecg, thalch, exang, oldpeak,slope, ca, thal):
    prediction = classifier.predict([[age, gender, cp, trestbps,chol, fbs, restecg, thalch, exang, oldpeak,slope, ca, thal]])
    return prediction

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
                exang = 0  
            else:
                exang = 1
        
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
            
        result = 0   
        if st.button("Predict", type="primary"):
            result = perdicton_func(age, gender, cp, trestbps,chol, fbs, restecg, thalach, exang, oldpeak,slope, ca, thal)
            if result == 0:
                st.success("The patient is Normal!")
            else:
                st.warning("The patient have Heart desies!")   

    with Data_info:
        # Add title to the page
        st.title("Data Info page")

        # Add subheader for the section
        st.subheader("View Data")

        # Create an expansion option to check the data
        with st.expander("View Raw data"):
            df = pd.read_csv("D://ML Project//HealthAI Predictive Suit//v1.0//Heart Desies prediction//heart.csv")
            st.dataframe(df)
            st.subheader("This Dataset After Preprocessing")
        
        # Create a section to columns values
        # Give subheader
        st.subheader("Columns Description:")

        # Create a checkbox to get the summary.
        if st.checkbox("View Summary"):
            st.dataframe(df.describe().T)

        # Create multiple check box in row
        col_name, col_dtype, col_data = st.columns(3)

        # Show name of all dataframe
        with col_name:
            if st.checkbox("Column Names"):
                st.dataframe(df.columns)

        # Show datatype of all columns 
        with col_dtype:
            if st.checkbox("Columns data types"):
                dtypes = df.dtypes.apply(lambda x: x.name)
                st.dataframe(dtypes)
        
        # Show data for each columns
        with col_data: 
            if st.checkbox("Columns Data"):
                col = st.selectbox("Column Name", list(df.columns))
                st.dataframe(df[col])     
                
    with Visualization:
        # Set the page title
        st.title("Visualise Some Demographics")

        # Create a checkbox to show correlation heatmap
        with st.expander("Show the correlation heatmap"):
            st.subheader("Correlation Heatmap")
            st.image("D:\ML Project\HealthAI Predictive Suit\images\heart\corelation.png")
        
        with st.expander("Show Diabetes Count")  : 
            st.subheader("Target Count Relation")
            st.image("D://ML Project//HealthAI Predictive Suit//images//heart//target.png")

        with st.expander("Show the Confusion Matrix"):
            st.subheader("Confusion Matrix")
            st.image("D:\ML Project\HealthAI Predictive Suit\images\heart\confmatrix.png")
            
        with st.expander("Show the Outliers"):
            st.subheader("Outliers Detection")
            st.image("D:\ML Project\HealthAI Predictive Suit\images\heart\outliers_1.png")
            
        with st.expander("Show the Outliers after removing"):
            st.subheader("Outliers Detection After Removing")
            st.image("D://ML Project//HealthAI Predictive Suit//images//heart//outliers_2.png")
            
        with st.expander("Show the test data"):
            st.subheader("Test Data Snipit : Psitive")
            st.image("D://ML Project//HealthAI Predictive Suit//images//heart//testdata.png")
            st.subheader("Result")
            st.image("D://ML Project//HealthAI Predictive Suit//images//heart//result_positive.png")
                            
if __name__ == '__main__':
    main()