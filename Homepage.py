import streamlit as st
import json
from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(
    page_title="Customer Propensty App",
    page_icon="fa-digital-ocean"
)

st.title("Customer Propensity App")
st.sidebar.success("Select a page")

def load_lottiefile(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)

lottie_team = load_lottiefile("lottiefiles/Hello.json")
st_lottie(
    lottie_team,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    # renderer="svg", # canvas
    height=300,
    width=None,
    key=None,
)



html_temp = """
    <div style="padding:10px">
    <h3 style="color:white;text-align:center;">This is a Customer Propensity App. Please go to the Models Page to enter the values and get the predictions </h3>
    </div>
    <div>
    <p>Propensity Models allow managers and analysts to identify potential customer opportunities in various groups of users and to improve user engagement. Propensity scores can be also directly used to create better marketing campaigns and targeting which will ultimately increase sales. It also reduces spending while ensuring better and faster decision-making.
    </p>
    </div>
    """
st.markdown(html_temp,  unsafe_allow_html=True)

image = Image.open('images/CPM.png')
st.image(image, caption='CPM Model')

image = Image.open('images/Churn.jpg')
st.image(image)


def load_lottiefile(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)
# if "input" not in  st.session_state:
#     st.session_state["input"] =
