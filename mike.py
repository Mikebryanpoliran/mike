import streamlit as st
import base64

st.set_page_config(page_title="Mike Blog", page_icon=":tada:")

st.markdown("""<h1 style='text-align: center; color: black; font-size: 2em; font-style: italic; font-family: "Times New Roman", serif;'>
            "Mike Blog"
            </h1>""", unsafe_allow_html=True)

st.write("---")
with st.container():
    left_column, right_column = st.columns((1,1))
    with left_column:
        st.write("""<div style="text-align: justify; font-family: serif; color: black;">My Journey as a Computer Engineering Student
                    In this technological era, We can’t imagine our
                    world now a days without internet as this mingled with our daily 
                    life very much and this is inseparable from us.Today man's scientific
                    knowledge is very wide advanced. In this generation the understanding 
                    and adaptation to things is bearly needed. Computers give humans a comfort 
                    on their needs and helps them to fulfill tasks. Job's and opportunities in 
                    It industry is highly in demand.</div>""", unsafe_allow_html=True)
        st.write("######")
        st.write("""<div style="text-align: justify; font-family: serif; color: black;">As my progress in my computer engineering studies, I have the opportunity 
                 to delve into specialized areas that align with your interests and aspirations.
                  Whether it's the intricate world of microprocessors, the vast domain of computer
                  networks, or the ever-expanding realm of software developing ,  and discover the 
                 niche that ignites my passion.</div>""", unsafe_allow_html=True)
    with right_column:
        st.image("mike.jpg")

st.write("""<div style="text-align: justify; font-family: serif; black:white;font-size: 1.1em; color:black;">My journey as a computer engineering student has been a transformative experience, shaping my 
         perspectives and opening up a world of possibilities. I have learned not only the technical skills 
         required to become a competent engineer but also the resilience, perseverance, and creativity essential 
         for success in this ever-evolving field.</div>""", unsafe_allow_html=True)
st.write("---")
st.write("###")

st.markdown("""<h1 style='text-align: center; color: black; font-size: 2em; font-style: italic; font-family: "Times New Roman", serif;'>
            About me
            </h1>""", unsafe_allow_html=True)

st.write("<div style= color: black; font-family: serif; color:black;>Name :Mike Bryan A. Poliran</div>",unsafe_allow_html=True)
st.write("<div style= color: black; font-family: serif;color:black;>Course :BSCpE 1A</div>",unsafe_allow_html=True) 
st.write("<div style= color: black; font-family: serif;color:black;>School :Surigao del norte state university</div>",unsafe_allow_html=True)
st.write("<div style= color: black; font-family: serif;color:black;>Age:18</div>",unsafe_allow_html=True)
st.write("<div style= color: black; font-family: serif;color:black;>Address :Brgy. Magsaysay, Placer SDN</div>",unsafe_allow_html=True)
st.write("<div style= color: black; font-family: serif;color:black;>Email:poliranmikebryan@gmail.com</div>",unsafe_allow_html=True)
st.write("<div style= color: black; font-family: serif;color:black;>Facebook: Mike Poliran</div>",unsafe_allow_html=True)

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
    
img = get_img_as_base64("haha.jpg")

page_bg_image = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/png;base64,{img}");
    background-size: cover;
}}

[data-testid="stHeader"]{{
    background-color: rgba(0, 0, 0, 0);
}}

</style>
"""

st.markdown(page_bg_image, unsafe_allow_html=True)
