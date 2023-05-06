#Streamlit app for autism diagnosis
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
    page = st.sidebar.selectbox("Select a page", ["Module1_Image_Classification", "Module2_Predictive_Analysis", "Module3_ Bidirectional_Encoder_Representations_from_Transformers"])

#for module 1- image classification
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
            print("")
#for Predictive Analysis
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

#for BERT
    elif page == "Module3_ Bidirectional_Encoder_Representations_from_Transformers":
                
        st.title("Question Answering with BERT")

        # Sample contexts and questions
        contexts = {
            "Baby Sleep": {
                "context": "As your baby gets a bit older, she won't need as many feeds during the night. As such, she'll be able to sleep for a bit longer. By this stage, some babies will even sleep for a full eight hours during the night (although, word of warning: don't get your hopes up). Most babies will spend twice as long sleeping at night as they do during the day – e.g. eight hours at night and four hours during the day.\nMany babies aged six months to a year will no longer need a night feed and may sleep for up to 12 hours at night. However, there're no guarantees of this, and some babies may wake up in the night for a bit (or a lot) longer.\nSometimes, your baby will nod off with seemingly no effort required from you. No rocking, no shushing, no patting. Then there are the nights where your baby will fight sleep as though their little life depends on it. What's more, once she does drop off, it won't be long before she's awake again. You know she needs to sleep, but she hasn't quite got the memo.\nFor nights like these, we've compiled a guide for getting your baby to sleep. Whether you give controlled crying a go, or experiment with using a dummy, there're a number of things you can do to up your chances of getting your baby to sleep.",
                "questions": ["how many hours do the six month old babies sleep?", "how to make my baby sleep?"]
            },
            "Autism": {
                "context": "Children with Autism Spectrum Disorder are often restricted, rigid, and even obsessive in their behaviors, activities, and interests. Symptoms may include: Repetitive body movements (hand flapping, rocking, spinning); moving constantly. Obsessive attachment to unusual objects (rubber bands, keys, light switches).",
                "questions": ["what are the traits of children with autism?"]
            }
        }

        # Sidebar to select context and question
        st.sidebar.title("Select Context and Question")
        context_choice = st.sidebar.selectbox("Context", list(contexts.keys()))
        question_choice = st.sidebar.selectbox("Question", contexts[context_choice]["questions"])

        # Display context and question
        st.header("Context:")
        st.write(contexts[context_choice]["context"])
        st.header("Question:")
        st.write(question_choice)


        # Answer question
        answer = answer_question(question_choice, contexts[context_choice]["context"])
        st.header("Answer:")
        st.write(answer)

if __name__ == "__main__":
    run()