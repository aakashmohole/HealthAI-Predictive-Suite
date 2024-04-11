import streamlit as st
import pickle

def main():
    ## Tabes 
    Prediction, Data_info, Visualization = st.tabs(["Prediction", "Dataset Overview", "Visualization"])
    with Prediction:     
        with st.form(key='columns_in_form'):
            c1, c2 = st.columns(2)
            c3, c4 = st.columns(2)
            c5, c6 = st.columns(2)
            c7, c8 = st.columns(2)
            c9, c10 = st.columns(2)
            c11, c12 = st.columns(2)
            c13, c14 = st.columns(2)
            c15 = st.columns(1)
            
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
                survival_months = st.number_input('Enter Survival Months', value=6)
            st.form_submit_button(label= 'Predict')
        
if __name__ == '__main__':
    main()
