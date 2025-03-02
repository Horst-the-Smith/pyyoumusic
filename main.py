#https://ja.linux-console.net/?p=26886

import streamlit as st
import datetime
from pytubefix import YouTube

st.title("Youtube Downloder")
st.session_state['URL'] = ("")
dt_now = datetime.datetime.now()

url = st.text_input('input any youtube URL')

button = st.button('Downlod!!')

if button:
    st.session_state.URL = (url)
    yt = YouTube(st.session_state.URL)
    yt.streams.first().download()

st.write(st.session_state.URL)
