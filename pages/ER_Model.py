import streamlit as st
from PIL import Image
from io import BytesIO
import base64




def get_image_download_link(img,filename,text):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href =  f'<a href="data:file/txt;base64,{img_str}" download="{filename}">{text}</a>'
    return href


def run():
    # set_bg_hack('db_1.png')
    image=Image.open('er_election_database.png')
    st.image(image,caption="ER Model")
    st.markdown(get_image_download_link(image,'ER_Model.png','Download ER Model'), unsafe_allow_html=True)

if __name__=='__main__':
    run()

