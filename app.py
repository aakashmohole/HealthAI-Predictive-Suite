import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.badges import badge
import pickle
import time
import os 
import utils.breast_cancer
import utils.diabetes
import utils.heart_desies
import utils.hypertension
import utils.stroke

## Side bar Menu
with st.sidebar:
    selected = option_menu('HealthAI Predictive Suite',
                          
                          ['Home',
                           'Breast Cancer Prediction',
                           'Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Hypertension Prediction',
                           'Stroke Prediction'],
                          icons=['house', 'lungs', 'thermometer', 'heart', 'sunrise', 'headphones'],
                          default_index=0)

# Diabetes Prediction Page
if(selected == 'Breast Cancer Prediction'):
    utils.breast_cancer.main()
elif(selected == 'Diabetes Prediction'):
    utils.diabetes.main()
elif(selected == 'Heart Disease Prediction'):
    utils.heart_desies.main()
elif(selected == 'Hypertension Prediction'):
    utils.hypertension.main()
elif(selected == 'Stroke Prediction'):
    utils.stroke.main()    
else:     
    ## Tabes 
    home, about, contact, deployment = st.tabs(["Home", "About Us", "Contact Us", "Deployment"])
    
    with home:
        
        badge(type="twitter", name="aakashmohole")
        ## Start
        st.title("HealthAI Predictive Suite")

        st.subheader("""
                    The "HealthAI Predictive Suite" is an application designed to provide predictive analytics in the field of healthcare.
                    """)

        st.write("""
                It encompasses multiple prediction models aimed at assisting healthcare professionals in making informed decisions and improving patient care. 
                Here's a detailed overview of the application:
                """)


        st.image('images/surgery.jpg')


        st.subheader('1. **Objective**:')
        st.write("""
                'The primary goal of the "HealthAI Predictive Suite" is to leverage machine learning algorithms to predict various health conditions based on input data.
                """)

        st.subheader('2. **Features**:')
        st.write("""- **Home Page**: Provides an overview of the application and its functionalities.
        - **Breast Cancer Prediction**: Predicts the likelihood of breast cancer occurrence based on patient data such as age, genetic factors, and medical history.
        - **Diabetes Prediction**: Predicts the risk of diabetes development using factors like age, weight, lifestyle, and family history.
        - **Heart Disease Prediction**: Estimates the probability of heart disease occurrence based on parameters like blood pressure, cholesterol levels, and lifestyle factors.
        - **Hypertension Prediction**: Predicts the risk of hypertension (high blood pressure) based on various health indicators.
        - **Stroke Prediction**: Predicts the likelihood of stroke occurrence using factors such as age, blood pressure, smoking status, and medical history.
        """)

        st.subheader('3. **Navigation**:')
        st.write("""
        - Users can navigate between different prediction models using a sidebar menu or navigation buttons.
        - The sidebar menu displays the list of available prediction models, allowing users to select the desired model for prediction.
        """)


        st.subheader('4. **Input Data**:')
        st.write("""
        - Each prediction model requires specific input data relevant to the respective health condition.
        - Users may need to input demographic information, medical history, lifestyle factors, and other relevant parameters to obtain predictions.
        """)

        st.subheader('5. **Prediction Outputs**:')
        st.write("""
            - After providing input data, the application generates predictions indicating the likelihood or risk level of the particular health condition.
            - Predictions are presented in a user-friendly format, often accompanied by explanations or recommendations.
        """)

        st.subheader('6. **Accuracy and Validation**:')
        st.write("""  
            - The prediction models are developed using machine learning techniques and undergo rigorous testing and validation to ensure accuracy and reliability.
            - Validation may involve using clinical data, cross-validation techniques, and comparison with established medical standards.
        """)

        st.subheader('7. **Ethical Considerations**:')
        st.write("""
            - Privacy and confidentiality of user data are prioritized, adhering to relevant regulations and guidelines.
            - Transparency regarding data usage, model assumptions, and limitations is provided to users.
        """)

        st.subheader("""Overall, the "HealthAI Predictive Suite" serves as a valuable tool for healthcare practitioners, researchers, and individuals interested in proactive health management. """)

    with about:
        badge(type="github", name="aakashmohole")
        
        st.title("""
                    Hello! I am Aakash Mohole!
                    """)
        st.write("""
                    I'm a dedicated B-Tech student with a profound interest in Data Science. I am committed to mastering the art of transforming raw data into actionable insights. 
                My academic pursuits have equipped me with a robust foundation in data analysis, machine learning, and data visualization.
                """)
        st.write("""
                    With an unwavering belief that every data point holds valuable information, I am actively seeking opportunities to apply my expertise to real-world challenges. 
                Whether it involves developing predictive models, facilitating data-driven decision-making, or crafting persuasive content, I am poised to make a substantial impact.
                I invite professionals and peers to connect, collaborate, and explore opportunities where data science and storytelling converge to drive innovation and positive change. 
                Together, we can navigate the dynamic landscape of data science and collectively shape a future driven by data-driven insights.
                """)
        
        with contact:
            st.title("Contact Me!")
            st.write("Have questions or feedback? Fill out the form below and we'll get back to you as soon as possible.")
            
            # Create form fields
            name = st.text_input("Name")
            email = st.text_input("Email")
            message = st.text_area("Message")
            
            # Submit button
            if st.button("Submit"):
                # Perform validation
                if not name:
                    st.error("Please enter your name.")
                elif not email:
                    st.error("Please enter your email.")
                elif not message:
                    st.error("Please enter your message.")
                else:
                    # Send the message (you can implement the sending logic here)
                    st.success("Your message has been sent successfully. We'll get back to you soon.")



        