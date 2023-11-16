import streamlit as st
from PIL import Image

st.title("Infrastructure: ")

img = Image.open(r"Infra1.jpg")
if img.size[0] < img.size[1]:
    img = img.rotate(90, expand=True)
st.image(img, caption='Outline of the system in our initial stage.')



img2 = Image.open(r"Infra2.jpg")
if img2.size[0] < img2.size[1]:
    img2 = img2.rotate(90, expand=True)
st.image(img2, caption='Outline of the system in our Final stage will be.')








