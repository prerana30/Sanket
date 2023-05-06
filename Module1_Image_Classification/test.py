import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

# Load the pre-trained model
model = tf.keras.models.load_model('my_model.h5')
def run():
    # Create a file upload widget for the user to upload an image
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    # When the user uploads an image, read it using PIL and pass it through the model
    if uploaded_file is not None:
        # Read the image using PIL
        image = Image.open(uploaded_file)
        
        # Preprocess the image for the model
        image = image.resize((224, 224))  # Resize the image to match the input size of the model
        image = np.asarray(image)  # Convert the image to a numpy array
        image = image / 255.0  # Normalize the pixel values
        image = np.expand_dims(image, axis=0)  # Add an extra dimension for the batch size
        
        # Pass the image through the model to make a prediction
        prediction = model.predict(image)
        print(prediction)
        # Display the prediction to the user
        if prediction[0][0] > prediction[0][1]:
            st.write("The model predicts that this image does not have autism.")
        else:
            st.write("The model predicts that this image has autism.")
run()