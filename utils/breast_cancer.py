import streamlit as st
import pickle
import pandas as pd

model = open("Models/bcp_rfmodel.pkl", "rb") 
classifier  = pickle.load(model)

def perdicton_func(age, race, material, tstage, nstage, sixstage, differentiate, grade, astage, tumor_size, estrogen, progesterone, regional_node, reginol_node_positive, survival_months):
    prediction = classifier.predict([[age, race, material, tstage, nstage, sixstage, differentiate, grade, astage, tumor_size, estrogen, progesterone, regional_node, reginol_node_positive, survival_months]])
    return prediction 


def main():
    ## Tabes 
    Prediction, Data_info, Visualization = st.tabs(["Prediction", "Dataset Overview", "Visualization"])
    with Prediction:     
        #with st.form(key='columns_in_form'):
        c1, c2 = st.columns(2)
        c3, c4 = st.columns(2)
        c5, c6 = st.columns(2)
        c7, c8 = st.columns(2)
        c9, c10 = st.columns(2)
        c11, c12 = st.columns(2)
        c13, c14 = st.columns(2)
        c15,c16 = st.columns(2)

        with c1:
            age = st.text_input("Age of person",value=0)
        with c2:
            race_option = st.selectbox(
                'Select Race',
                ('White', 'Black', 'Other'))
            if race_option == 'White':
                race = 0    
            elif race_option == 'Black':
                race = 1
            else :  race = 2
            
        with c3:
            material_option = st.selectbox(
                'Select Marital Status',
                ('Married', 'Single', 'Divorced', 'Widowed', 'Separated'))
            if material_option == 'Married':
                material = 0    
            elif material_option == 'Single':
                material = 1
            elif material_option == 'Divorced':
                material = 2
            elif material_option == 'Widowed':
                material = 3
            else :  material = 4
            
        with c4:
            tstage_option = st.selectbox(
                'Select T Stage',
                ('T1', 'T2', 'T3', 'T4'))
            if tstage_option == 'T1':
                tstage = 0    
            elif tstage_option == 'T2':
                tstage = 1
            elif tstage_option == 'T3':
                tstage = 2
            else :  tstage = 3
        
        with c5:
            nstage_option = st.selectbox(
                'Select N Stage',
                ('N1', 'N2', 'N3'))
            if nstage_option == 'N1':
                nstage = 0    
            elif nstage_option == 'N2':
                nstage = 1
            else :  nstage = 2
        
        with c6:
            sixstage_option = st.selectbox(
                'Select 6th Stage',
                ('IIA', 'IIB', 'IIIA', 'IIIC', 'IIIB'))
            if sixstage_option == 'IIA':
                sixstage = 0    
            elif sixstage_option == 'IIB':
                sixstage = 1
            elif sixstage_option == 'IIIA':
                sixstage = 2
            elif sixstage_option == 'IIIC':
                sixstage = 3
            else :  sixstage = 4
            
        with c7:
            differentiate_option = st.selectbox(
                'Select differentiate',
                ('Moderately differentiated', 'Poorly differentiated', 'Well differentiated', 'Undifferentiated'))
            if differentiate_option == 'Moderately differentiated':
                differentiate = 0    
            elif differentiate_option == 'Poorly differentiated':
                differentiate = 1
            elif differentiate_option == 'Well differentiated':
                differentiate = 2
            else :  differentiate = 3
            
        with c8:
            grade = st.number_input("Enter Grade (1-3)")
        
        with c9:
            astage_options = st.selectbox('Select A Stage',
                                            ('Regional','Distant'))
            
            if astage_options == 'Regional':
                astage = 0
            else: astage = 1
        
        with c10:
            tumor_size = st.number_input('Enter Tumor Size (int)', value=35)
            
        with c11:
            estroge_options = st.selectbox('Select Estrogen Status',
                                            ('Positive','Negative'))
            if estroge_options == 'Positive':
                estrogen = 0
            else: estrogen = 1   
            
        with c12 :
            progesterone_options = st.selectbox('Select  Progesterone Status',
                                            ('Positive','Negative'))
            if progesterone_options == 'Positive':
                progesterone = 0
            else: progesterone = 1
            
        with c13 :
            regional_node = st.number_input('Enter Regional Node Examined (int)', value=14)
            
        with c14:
            reginol_node_positive = st.number_input('Enter Reginol Node Positive', value=6)
            
        with c15:
            survival_months = st.number_input('Enter Survival Months', value=3)
        
        result = 0   
        if st.button("Predict", type="primary"):
            result = perdicton_func(age, race, material, tstage, nstage, sixstage, differentiate, grade, astage, tumor_size, estrogen, progesterone, regional_node, reginol_node_positive, survival_months)
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
            df = pd.read_csv("v1.0/Breast Cancer Prediction/Breast_Cancer.csv")
            st.dataframe(df)
            st.subheader("This is Raw Dataset Befor Preprocessing")
            
        with st.expander("View Cleaned data"):
            df_clean= pd.read_csv("v1.0/Breast Cancer Prediction/cleaneddata.csv")
            st.dataframe(df_clean)
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
            st.image("images/Breast Cancer/corelation.png")
        
        with st.expander("Show the Dead Alive Count")  : 
            st.subheader(" Dead Alive Relation")
            st.image("images/Breast Cancer/dead_alive.png")

        with st.expander("Show the Material Status"):
            st.subheader("Material Status")
            st.image("images/Breast Cancer/material_status.png")
            
        with st.expander("Show the Outliers"):
            st.subheader("Outliers Detection")
            st.image("images/Breast Cancer/outliers.png")
if __name__ == '__main__':
    main()
