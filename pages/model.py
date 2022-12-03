import time
import requests

import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

import random
from streamlit_d3_demo import d3_line

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def generate_random_data(x_r, y_r):
    return list(zip(range(x_r), [random.randint(0, y_r) for _ in range(x_r)]))

lottie_url_hello = "https://assets5.lottiefiles.com/packages/lf20_V9t630.json"
lottie_url_download = "https://assets4.lottiefiles.com/private_files/lf30_t26law.json"
lottie_hello = load_lottieurl(lottie_url_hello)
lottie_download = load_lottieurl(lottie_url_download)


st_lottie(lottie_hello, key="hello")

if st.button("Download"):
    with st_lottie_spinner(lottie_download, key="download"):
        time.sleep(5)
    st.balloons()
    d3_line(generate_random_data(20, 500), circle_radius=15, circle_color="#6495ed")



