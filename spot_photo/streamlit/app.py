#ICI ON BUILD NOTRE INTERFACE
import streamlit as st
import requests
from google.oauth2 import service_account
from google.cloud import storage
from PIL import Image
from io import BytesIO

st.title(" Welcome to Spot Photo 🔍 ")
st.subheader("A wonderful app to look after your f**cking holidays pictures during dark and rainy days")


model_choice = st.selectbox('Please select a model', ('all-mpnet-base-v2', 'clip-ViT-B-32'))


query = st.text_input('Which photo are you looking for ?', 'Please enter your description')


k = st.slider('Number of pictures to display', 1, 5, 3)


if query is not None:
    params = dict(model_choice=model_choice, query=query, k=k, )


    spot_photo_api_url = 'http://127.0.0.1:8000/recherche'
    response = requests.get(spot_photo_api_url, params=params)

    if response.ok:
        #st.markdown(f'{response.json()}')

        credentials = service_account.Credentials.from_service_account_file('possible-aspect-369317-b19475afaf02.json')

        client = storage.Client(credentials=credentials)
        #client = storage.Client('possible-aspect-369317')
        bucket_name = 'bucket_image_flickr30k'

        bucket = client.get_bucket(bucket_name)

        blob_l =[]
        d = response.json()
        for image in d.keys() :
            file_name = f"flickr30k_images/{image}"
            blob = bucket.get_blob(file_name)
            blob_l.append(blob)
        rows = len(d.keys())
        for x in range(rows):
            blob_n = blob_l[x]
            img = Image.open(BytesIO(blob_n.download_as_bytes()))
            st.image(img)
    else:
        st.write(response.json())
