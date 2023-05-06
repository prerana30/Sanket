import streamlit as st
from PIL import Image
import numpy as np
import Module1_Image_Classification
import Module2_Predictive_Analysis
import tensorflow as tf
import spacy

# Load the pre-trained model
model = tf.keras.models.load_model('my_model.h5')
def run():
    st.title("Sanket")
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a page", ["Module1_Image_Classification", "Module2_Predictive_Analysis", "Module3_Names_Entity_Recognition"])

    if page == "Module1_Image_Classification":
        st.write("Please upload an image for classification:")
        image_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
        print(image_file)
        if image_file is not None:
            image = Image.open(image_file)
            image = image.resize((224, 224))  # Resize the image to match the input size of the model
            image = np.asarray(image)  # Convert the image to a numpy array
            image = image / 255.0  # Normalize the pixel values
            image = np.expand_dims(image, axis=0)  # Add an extra dimension for the batch size
            
            # Pass the image through the model to make a prediction
            prediction = model.predict(image)
            
            # Display the prediction to the user
            if prediction[0][0] > prediction[0][1]:
                st.write("The model predicts that this image does not have autism.")
            else:
                st.write("The model predicts that this image has autism.")
        else:
            print("NOT RUNNNNNNN")

    elif page == "Module2_Predictive_Analysis":
        st.title("Predictive Analysis")
        st.write("Please fill out the questionnaire:")
        questionnaire = {}
        questionnaire['Q1'] = st.selectbox("Does your child look at you when you call his/her name?", ["Always", "Usually", "Sometimes", "Rarely", "Never"])
        questionnaire['Q2'] = st.selectbox("How often it is easy for you to get eye contact with your child?", ["Always", "Usually", "Sometimes", "Rarely", "Never"])
        questionnaire['Q3'] = st.selectbox("Does your child point to indicate that she/he wants something?", ["Always", "Usually", "Sometimes", "Rarely", "Never"])
        questionnaire['Q4'] = st.selectbox("Does your child point to share interest with you?", ["Always", "Usually", "Sometimes", "Rarely", "Never"])
        questionnaire['Q5'] = st.selectbox("Does your child pretend?", ["Always", "Usually", "Sometimes", "Rarely", "Never"])
        questionnaire['Q6'] = st.selectbox("If you or someone else in the family is visibly upset, does your child show signs of wanting to comfort them?", ["Always", "Usually", "Sometimes", "Rarely", "Never"])
        questionnaire['Q7'] = st.selectbox("Does your child use simple gesture?", ["Always", "Usually", "Sometimes", "Rarely", "Never"])
        questionnaire['Q8'] = st.selectbox("Does your child stare at nothing with no apparent purpose?", ["Always", "Usually", "Sometimes", "Rarely", "Never"])
        questionnaire['Q9'] = st.selectbox("Does your child follow where you're looking?", ["Always", "Usually", "Sometimes", "Rarely", "Never"])
        questionnaire['Q10'] = st.text_input("How would you describe your child's first word as:")
        questionnaire['age'] = st.text_input("What is the age of your child?")
        questionnaire['gender'] = st.selectbox("What is the gender of your child?", ["Male", "Female"])
        questionnaire['jaundice'] = st.selectbox("Was your child Born with jaundice?", ["Yes", "No"])
        questionnaire['family_history'] = st.selectbox("Is any of your immediate family members have a history with ASD?", ["Yes", "No"])
        questionnaire['completed_by'] = st.text_input("Who is completing the test?")
        

        q1 = ["Always", "Usually", "Sometimes", "Rarely", "Never"].index(questionnaire['Q1'])
        q2 = ["Always", "Usually", "Sometimes", "Rarely", "Never"].index(questionnaire['Q2'])
        q3 = ["Always", "Usually", "Sometimes", "Rarely", "Never"].index(questionnaire['Q3'])
        q4 = ["Always", "Usually", "Sometimes", "Rarely", "Never"].index(questionnaire['Q4'])
        q5 = ["Always", "Usually", "Sometimes", "Rarely", "Never"].index(questionnaire['Q5'])
        q6 = ["Always", "Usually", "Sometimes", "Rarely", "Never"].index(questionnaire['Q6'])
        q7 = ["Always", "Usually", "Sometimes", "Rarely", "Never"].index(questionnaire['Q7'])
        q8 = ["Always", "Usually", "Sometimes", "Rarely", "Never"].index(questionnaire['Q8'])
        q9 = ["Always", "Usually", "Sometimes", "Rarely", "Never"].index(questionnaire['Q9'])
            # Process the answers to calculate the score
        score = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9
        
        # Determine the result based on the score
        if score <= 6:
            result = "Low risk of autism"
        elif score <= 12:
            result = "Moderate risk of autism"
        else:
            result = "High risk of autism"
        
        # Display the result to the user
        st.write("Based on your answers, your child has a", result)

if __name__ == "__main__":
    run()