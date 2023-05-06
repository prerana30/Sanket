#import necessary libraries
import streamlit as st
from numpy import *

def run(questionnaire):
    
    # Convert the answers to integers
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