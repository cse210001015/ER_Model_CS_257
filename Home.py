import streamlit as st
import base64
from PIL import Image

def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

def run():
    set_bg_hack('db_2.png')
    st.title("CS 257 Mid Evaluation:Database Design Using ER model")
    
    
if __name__=='__main__':
    run()
