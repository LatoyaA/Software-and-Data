import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
import pathlib
from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array


header = st.container()

# Page formatting and image display
with header:
    st.set_option('deprecation.showfileUploaderEncoding', False)
    co1, col2, col3 = st.columns(3)
    col2.image('planting.jpeg', width=240, output_format='jpeg')

with header:
    st.markdown("<h1 style='text-align: center; color: green;'>PlantIng</h1>", unsafe_allow_html=True)


with header:
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('')


with header:
    st.text('')
    st.markdown("<h3 style='text-align: center; color: green;'>Welcome to PlantIng, your ultimate guide to learning about houseplants</h3>", unsafe_allow_html=True)

    st.text('')
    st.text('')
    st.text('')
    st.markdown("<h3 style='text-align: center; color: green;'>PlantIng identifies your houseplants with instant results, and returns your compatibility. </h3>", unsafe_allow_html=True)
    st.text('')
    st.text('')
    st.markdown("<h5 style='text-align: left; color: black;'> Please upload an image of the FLOWER from plant you would like to identify. </h5", unsafe_allow_html=True)


#file selector, upload from your pc
uploaded_file = st.file_uploader("Upload an image", type=("png", "jpg", "jpeg"))


if uploaded_file is not None:
    # load and preprocess the image
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    img = img.resize((224,224))
    img = img_to_array(img)
    X_list = []
    X_list.append(img)
    X = np.stack(X_list, axis = 0)

#load data_dir and predict

    url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
    data_dir = tf.keras.utils.get_file('flower_photos', origin=url, untar=True)
    data_dir = pathlib.Path(data_dir)
    # key for renaming columns
    rename_columns ={0: 'daisy', 1: 'dandelion', 2: 'roses', 3: 'sunflowers', 4: 'tulips'}

#----------------------------------------------------------------
