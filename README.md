# Sanket : Autism detection web app
<h3> Sanket is a webapp for the early detection of autism spectrum disorder and counseling.
</h3>

<h2>Do you know what autism really is?</h2>
<h3>
Autism Spectrum Disorder (ASD) is a neurodevelopmental disorder that affects social interaction, communication, and behavior. Individuals with ASD may have difficulty with social skills such as eye contact, nonverbal communication, and forming friendships. They may also have repetitive behaviors or limited interests, and may struggle with sensory processing issues.</h3>

<h2>What we are going to do in our project?</h2>
<h3>1. Our webapp aims to detect Autism Spectrum Disorder in patients using three modules

- First Module has the ability classify the patient based on an image fed into the system, providing a result that is carried forward to Module 2 for further accuracy.
- Module 2 Asks the parent or guardian of the patient a set of questions related to the patient's behavior to make a classification based on the answers.
- Last module provides a bridge between the intelligent system and the parent/guardian, allowing them to ask any questions related to Autism or ASD and providing answers to those queries using BERT.

</h3>
<h3>2. Aims to improve accuracy of diagnosis using a combination of patient behavior analysis and image recognition.
</h3>
<h3>
4. Provides a user-friendly interface for parents/guardians to interact with the system and ask questions related to Autism or ASD.
</h3>
<h3>
5. Includes measures to ensure security and privacy of patient data.
</h3>
<h3>
6.Incorporates ongoing maintenance, updates, and technical support for the system after launch.</h3>

<h2>Software Tools we used</h2>
<h3>We downloaded all this software tools in virtual environment:
Creating Virtual environment in Windows by typing "python -m venv myenv" in terminal. 
And then Activate the virtual environment by running the command "myenv\Scripts\activate
".


</h3>

<h3>
- Python
- Numpy
- Pandas
- Matplotlib
- Stream-lit
- Keras
- Tensorflow
- Pillow
- CNN
- NLP
</h3>

<h2>Running Instructions:</h2>
<h3> pip install Numpy, pandas, tensorflow, streamlit, pillow </h3>
<h3></br>
For binary image classification we used CNN algorithm.This helps us to detect a child has autism or not. You may be curious,why we use CNN?
As you know, we have to classify the images of children by facial features.
</h3></br>
 
1. For binary image classification, </br>
- We firstly, import the necessary keras models.</br>
-Then, most importantly we generate batches of tensor image data with real time augmentation to be able to recognise new unseen images by prevention of overfitting.</br>
- The script defines two ImageDataGenerator objects and 'flow_from_directory' method is used to load the data into the model.</br>

- The CNN model is built using the Sequential model object. This demonstrates how to build a CNN model for binary image classification using Keras.</br>


