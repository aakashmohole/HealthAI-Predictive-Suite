import streamlit as st
import pickle
import pandas as pd

model = open("Models/stroke_rfmodel.pkl", "rb") 
classifier  = pickle.load(model)

def perdicton_func(sex, age, hypertension, heartdesies, married, worktype, residencetype, oldpeak, bmi, smoke):
    prediction = classifier.predict([[sex, age, hypertension, heartdesies, married, worktype, residencetype, oldpeak, bmi, smoke]])
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
        
        with c1:
            sex_option = st.selectbox(
                'Select Gender',
                ('Male', 'Female'))
            if sex_option == 'Male':
                sex = 1    
            else:
                sex = 0
        
        with c2:
                age = st.text_input("Age of person",value=0)
            
        with c3:
            hypertension_option = st.selectbox(
                'Select patient has ever had hypertension',
                ('Yes', 'No'))
            if hypertension_option == 'Yes':
                hypertension = 1  
            else: hypertension = 0
            
        with c4:
            heartdesies_option = st.selectbox(
                'Select patient has ever had heart dieses!',
                ('Yes', 'No'))
            if heartdesies_option == 'Yes':
                heartdesies = 1  
            else: heartdesies = 0

        with c5:
            married_option = st.selectbox(
                'Patient married or not?',
                ('Marrid', 'Single'))
            if married_option == 'Married':
                married = 1      
            else:
                married = 0
        with c6:
            worktype_option = st.selectbox(
                'Select patient work type: ',
                ('Never worked', 'Children', 'Govt job','Self-employed','Private'))
            if worktype_option == 'Never worked':
                worktype = 0  
            elif worktype_option == 'Children':
                worktype = 1
            elif worktype_option == 'Govt job':
                worktype = 2
            elif worktype_option == 'Self-employed':
                worktype = 3
            else : worktype = 4
        
        with c7:
            residencetype_option = st.selectbox(
                'Select patient area:',
                ('Urban', 'Rural'))
            if residencetype_option == 'Urban':
                residencetype =  1
            else:
                residencetype = 0
        
        with c8:
            oldpeak = st.number_input('Patient average blood sugar level', value=228.69)
            
        with c9 :
            bmi = st.number_input('Body Mass Index', value=36.6)
            

        with c10:
            smoke_option = st.selectbox(
                'Smoked or not?',
                ('Smokes', 'Never Smoked'))
            if smoke_option == 'Smokes':
                smoke = 1
            else: smoke =0
            
        result = 0   
        if st.button("Predict", type="primary"):
            result = perdicton_func(sex, age, hypertension, heartdesies, married, worktype, residencetype, oldpeak, bmi, smoke)
            if result == 0:
                st.success("The patient is Normal!")
            else:
                st.warning("The patient is in stroke!")    
    
    with Data_info:
        # Add title to the page
        st.title("Data Info page")

        # Add subheader for the section
        st.subheader("View Data")

        # Create an expansion option to check the data
        with st.expander("View Raw data"):
            df = pd.read_csv("v1.0/Stroke Prediction/stroke_data.csv")
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
            st.image("images/stroke/corelation.png")
        
        with st.expander("Show Diabetes Count")  : 
            st.subheader("Target Count Relation")
            st.image("images/stroke/stroke.png")

        with st.expander("Show the Confusion Matrix"):
            st.subheader("Confusion Matrix")
            st.image("images/stroke/confmatrix.png")
            
        with st.expander("Show the Outliers"):
            st.subheader("Outliers Detection")
            st.image("images/stroke/outliers.png")
            
        with st.expander("Show the test data"):
            st.subheader("Test Data Snipit : Psitive")
            st.image("images/stroke/testdata.png")
            st.subheader("Result")
            st.image("images/stroke/result.png")

if __name__ == '__main__':
    main()