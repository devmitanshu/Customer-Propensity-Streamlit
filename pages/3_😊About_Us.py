import streamlit as st
from streamlit_lottie import st_lottie
import json


st.title("About Us")
st.sidebar.success("Select a page")


def load_lottiefile(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)


lottie_team = load_lottiefile("lottiefiles/team.json")
st_lottie(
    lottie_team,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",  # medium ; high
    # renderer="svg", # canvas
    height=None,
    width=None,
    key=None,
)

st.markdown(f'<h3 style = "color:yellow;text-align:center;">We are the Students of NMIMS Indore</h3>',unsafe_allow_html=True)
st.markdown(f'<h3 style = "text-align:center; font-size:30px">Jay Sarode</h3>',unsafe_allow_html=True)
st.markdown(f'<h3 style = "text-align:center; font-size:30px">Jaanvi Porwal</h3>',unsafe_allow_html=True)
st.markdown(f'<h3 style = "text-align:center; font-size:30px">Mitanshu Holkar</h3>',unsafe_allow_html=True)
st.markdown(f'<h3 style = "text-align:center; font-size:30px">Palak Jain</h3>',unsafe_allow_html=True)
st.markdown(f'<h3 style = "color:yellow;text-align:center;">B.Tech CSBS 4th Year</h3>',unsafe_allow_html=True)


    
    
            
