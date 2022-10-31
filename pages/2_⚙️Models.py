import streamlit as st
import numpy as np
import pandas as pd
import pickle

st.title("Model")
st.sidebar.success("Select a page")

# pickle_in = open("model.pkl", "rb")
# model = pickle.load(pickle_in)


# def predict_genres(customer_id, order_estimated_delivery_date, order_delivered_customer_date,freight_value, order_item_id, customer_state, product_category_name_english, product_name_lenght, product_description_lenght, product_photos_qty):
    
#     """Let's Classify Music genres using these parameters
#     """
#     prediction = model.predict([[customer_id, order_estimated_delivery_date, order_delivered_customer_date,freight_value, order_item_id, customer_state, product_category_name_english, product_name_lenght, product_description_lenght, product_photos_qty]])
#     print(prediction)
#     return prediction

def main():
    st.markdown(f'<h3 style = "color:yellow;text-align:center;">Predicting Customer Propensity to Churn</h3>', unsafe_allow_html=True)
    html_temp = """
    <div style="padding:10px">
    <h3 style="color:white;text-align:center;">Enter the Customer Details</h3>
    </div>
    """
    st.markdown(html_temp,  unsafe_allow_html=True)
    customer_id = st.text_input("Enter Customer ID", "")
    order_estimated_delivery_date = st.text_input("Enter Estimate Delivery Date", "")
    order_delivered_customer_date = st.text_input("Enter Order Delivered Customer Date", "")
    freight_value = st.text_input("Enter Freight Value", "")
    order_item_id = st.text_input("Enter Order Item Id", "")
    customer_state = st.text_input("Enter Customer State", "")
    product_category_name_english = st.text_input("Enter Product Category Name English", "")
    product_name_lenght = st.text_input("Enter Product Name Lenght", "")
    product_description_lenght = st.text_input("Enter Product Description Lenght", "")
    product_photos_qty = st.text_input("Enter Product Photos Quantity", "")
    
    result=""
    if st.button("Predict"):
        result=predict_genres(customer_id, order_estimated_delivery_date, energy, instrumentalness, liveness, speechiness, tempo, valence)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Made with love by the students of NMIMS Indore <3")

if __name__ == "__main__":
    main()