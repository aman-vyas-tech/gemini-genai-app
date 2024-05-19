from dotenv import load_dotenv

load_dotenv() #load all env variab
import streamlit as st
import  os
import google.generativeai as genai
from PIL import Image
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input, image):
    if input!= "":
        response=model.generate_content([input, image])
    else:
        resource=model.generate_content(image)
    return response

## Initialize our streamlet app

st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Gen AI Application")

input= st.text_input("Input: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Upload Image to Gen AI")

if submit:
    response= get_gemini_response(input, image)
    st.subheader("The response is")
    st.write(response.text)
    st.write(response.candidates)
