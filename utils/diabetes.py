import streamlit as st
import pickle
import pandas as pd

model = open("Models/dtmodel.pkl", "rb") 
classifier  = pickle.load(model)

def perdicton_func(age, gender, high_cholesterol, five_year_cholesterol, bmi, smoker, HeartDiseaseorAttack, PhysActivity, fruits, veggis,  HvyAlcoholConsump, GenHlth, MentHlth, PhysHlth, DiffWalk, Stroke, HighBP):
    prediction = classifier.predict([[age, gender, high_cholesterol, five_year_cholesterol, bmi, smoker, HeartDiseaseorAttack, PhysActivity, fruits, veggis,  HvyAlcoholConsump, GenHlth, MentHlth, PhysHlth, DiffWalk, Stroke, HighBP]])
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
        c17, c18 = st.columns(2)
        
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
            cholesterol_option = st.selectbox(
                'Select High Cholesterol',
                ('No high cholesterol', 'High cholesterol'))
            if cholesterol_option == 'No high cholesterol':
                high_cholesterol = 0  
            else:
                high_cholesterol = 1
            
        with c4:
            five_years_cholesterol_option = st.selectbox(
                'Select High Cholesterol',
                ('No cholesterol check in 5 years', 'High cholesterol'))
            if five_years_cholesterol_option == 'No cholesterol check in 5 years':
                five_year_cholesterol = 0  
            else:
                five_year_cholesterol = 1
        
        with c5:
            bmi = st.number_input("Enter Body Mass Index (BMI)")
        with c6:
            smoker_option = st.selectbox(
                'Smoker (Have person smoked at least 100 cigarettes in your entire life?)',
                ('Yes', 'No'))
            if smoker_option == 'No':
                smoker = 0  
            else:
                smoker = 1
            
        with c7:
            HeartDiseaseorAttack_option = st.selectbox(
                'Coronary heart disease (CHD) or myocardial infarction (MI) ',
                ('Yes', 'No'))
            if smoker_option == 'No':
                HeartDiseaseorAttack = 0  
            else:
                HeartDiseaseorAttack = 1
            
        with c8:
            PhysActivity_option = st.selectbox(
                'Physical activity in past 30 days - not including job ',
                ('Yes', 'No'))
            if PhysActivity_option == 'No':
                PhysActivity = 0  
            else:
                PhysActivity = 1
        
        with c9:
            fruits_option = st.selectbox(
                'Consume Fruit 1 or more times per day',
                ('Yes', 'No'))
            if fruits_option == 'No':
                fruits = 0  
            else:
                fruits = 1
        
        with c10:
            veggis_option = st.selectbox(
                'Consume Vegetables 1 or more times per day',
                ('Yes', 'No'))
            if veggis_option == 'No':
                veggis = 0  
            else:
                veggis = 1
            
        with c11:
            HvyAlcoholConsump_option = st.selectbox(
                'Consume Heavy Alcohol',
                ('Yes', 'No'))
            if HvyAlcoholConsump_option == 'No':
                HvyAlcoholConsump	 = 0  
            else:
                HvyAlcoholConsump	 = 1
            
        with c12 :
            GenHlth_options = st.selectbox('Select  Genral Health',
                                            ('Excellent','Very good','Good', 'Fair', 'Poor'))
            if GenHlth_options == 'Excellent':
                GenHlth = 1
            elif GenHlth_options == 'Very good':
                GenHlth = 2
            elif GenHlth_options == 'Good':
                GenHlth = 3 
            elif GenHlth_options == 'Fair':
                GenHlth = 4
            else:
                GenHlth = 5
            
        with c13 :
            MentHlth = st.number_input('Enter days of poor mental health scale 1-30 days', value=14)
            
        with c14:
            PhysHlth = st.number_input('Enter physical illness or injury days in past 30 days scale 1-30', value=6)
            
        with c15:
            DiffWalk_option = st.selectbox(
                'Do you have serious difficulty walking or climbing stairs?',
                ('Yes', 'No'))
            if DiffWalk_option == 'No':
                DiffWalk = 0  
            else:
                DiffWalk = 1
        with c16:
            Stroke_option = st.selectbox(
                'Person ever had a stroke',
                ('Yes', 'No'))
            if Stroke_option == 'No':
                Stroke = 0  
            else:
                Stroke = 1
        
        with c17:
            HighBP_option = st.selectbox(
                'Person ever had a High BP',
                ('No high, BP', 'High BP'))
            if HighBP_option == 'No high, BP':
                HighBP = 0  
            else:
                HighBP = 1
        
        result = 0   
        if st.button("Predict", type="primary"):
            result = perdicton_func(age, gender, high_cholesterol, five_year_cholesterol, bmi, smoker, HeartDiseaseorAttack, PhysActivity, fruits, veggis,  HvyAlcoholConsump, GenHlth, MentHlth, PhysHlth, DiffWalk, Stroke, HighBP)
            if result == 0:
                st.success("The persion is Alive")
            else:
                st.warning("The Person is dead!")
    
    with Data_info:
        # Add title to the page
        st.title("Data Info page")

        # Add subheader for the section
        st.subheader("View Data")

        # Create an expansion option to check the data
        with st.expander("View Raw data"):
            df = pd.read_csv("v1.0/Diabetes Prediction/diabetes_data.csv")
            st.dataframe(df)
            st.subheader("This Dataset After Preprocessing")
        
        # Create a section to columns values
        # Give subheader
        st.subheader("Columns Description:")

        # Create a checkbox to get the summary.
        if st.checkbox("View Summary"):
            st.dataframe(df.describe())

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
            st.image("images/Diabetes/corelasion.png")
        
        with st.expander("Show Diabetes Count")  : 
            st.subheader("Diabetes Count Relation")
            st.image("images/Diabetes/diabetes.png")

        with st.expander("Show the Confusion Matrix"):
            st.subheader("Confusion Matrix")
            st.image("images/Diabetes/confusionmatrix.png")
            
        with st.expander("Show the Outliers"):
            st.subheader("Outliers Detection")
            st.image("images/Diabetes/outliers.png")
            
        with st.expander("Show the Outliers after removing"):
            st.subheader("Outliers Detection After Removing")
            st.image("images/Diabetes/afterremoveoutliers.png")
if __name__ == '__main__':
    main()