import streamlit as st # to import the functions to design the interface
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai 

from PIL import Image 

# Streamlit Page
st.set_page_config(page_title='Structural Defect Analysis Using AI',page_icon = '🤖🧠🇦🇮👾',layout='wide')
st.title('AI Assistant for :green[Structural Defect Analysis]🤖🧠🇦🇮👾')
st.header(':blue[Prototype for automated structural defect analysis]🛠️')
st.subheader('''Develop a web based app using Streamlit that allows users to upload image of a building structure and to analyze the effect using Generative AI model.''')

with st.expander('➤About the application'):
    st.markdown(f'''This is used to detect the structural defect in building images like cracks,misallignments using AI system
                ***Defect Detection***
                ***Recommendation***
                ***Report Generation***''')
    
st.subheader('Upload the image here📁')
    
input_image = st.file_uploader('Click here👉',type=['png','jpg','jpeg'])
img = ''
    
if input_image:
    img = Image.open(input_image).convert('RGB')
    st.image(img,caption='Uploaded Successfully✅')
    
prompt = f'''Act as a structural and civil engineer and provide the necessary details in the proper bullet points in more precise way (maximum 3 points) for the following questions:
1. Is there any structural defect such as cracks, bends, damages in the given image
2. What is the probablity of the detected defect?
3. What is the severity level of the defect like minor, moderate or major?
4. What is the possible cause for the given defect, considering the material damage, environmental damage?
5. Say whether we can repair this defector not? If not say whether we need to replace this or not?
6. SUggest the remedies to repair the defect.
7. Say whether the defect will cause any damage to the surrounding and give probablity for that.
8. Say whether we need to monitor the defected area after repair or replacements?
9. Give the cost range in Indian rupees.
10. Generate summary on the insights.

'''

import os

ai_key = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=ai_key)

def generate_results(prompt,img):
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    results = model.generate_content(f'''Using the given prompt{prompt},
                                     analyze the given image{img} and 
                                     generate the results based on the prompt''')
    return results.text

submit = st.button('Analyze the defect🔍')

if submit:
    with st.spinner('Analyzing.....🤔'):
        response = generate_results(prompt,img)
    
        st.markdown('## :green[Results🎯]')
        st.write(response)
        