# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import google.generativeai as genai
import os
from PIL import Image 
os.environ['GOOGLE_API_KEY']='AIzaSyAVcFO11u1AyG8v-fnTXw9996mceUDF_X4'
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

def get_gemini_response(aimodel,input,image):
    # Use a breakpoint in the code line below to debug your script.
    model = genai.GenerativeModel(aimodel)
    if aimodel=='gemini-pro':
        response=model.generate_content(input)
    else:
        if input!='':
            response = model.generate_content([input,image])
        else:
            response = model.generate_content(image)

    return response.text

st.set_page_config(page_title='GenAI',layout="wide")
st.header('Gemini Application')

# Define dropdown options and default value
options = ['gemini-pro', 'gemini-pro-vision']
default_value = 'gemini-pro'
col1, col2, col3 = st.columns([1, 3, 1])  # Initialize with two columns and adjust width ratio

# Dropdown in the first column
selected_option = col1.selectbox("Select an option:", options, index=options.index(default_value), key="dropdown",
                                 help="Dropdown")

# Input text box in the second column
inp = col2.text_input('Input: ', key='input')

# Image upload in the third column (conditional based on dropdown value)
image = None
if selected_option == 'gemini-pro-vision':
    # If gemini-pro-vision is selected, update the columns layout
    #col1, col2, col3 = st.columns([1, 1, 1])  # Adjust the width ratio for three columns

    # Display the custom CS

    uploaded_image = col3.file_uploader("Upload Image", type=['jpg', 'jpeg', 'png'], key="image_upload",
                                         help="Image upload")
    # Hide the default "Drag and drop file here" message using custom CSS and JavaScript
    image=Image.open(uploaded_image)
    #inp = col3.text_input('Input: ', key='input1')
submit=st.button('Ask')
if submit:
    response=get_gemini_response(selected_option,inp,image)
    st.subheader('The Response is')
    st.write(response)
