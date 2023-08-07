#Connect this PyCharm file to a GitHub Repo labeled 'st-hello-world'
#Connect that GitHub Repo to Streamlit for hosting services

import streamlit as st
from PIL import Image

st.header("Streamlit App")
st.subheader("Programmed in PyCharm, Pushed to GitHub, and Hosted by Streamlit")
st.write("Hello World! It's great to meet you.")

image = Image.open('sunrise_coastline.png')
st.image(image, caption='Sunrise on the coast.')