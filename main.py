import streamlit as st
import pandas as pd



st.set_page_config(layout="wide")

st.header("My company")
st.write("My team consists of 12 members")
st.subheader("Team info")

col1, col2, col3= st.columns(3)

df = pd.read_csv(r"C:\Users\MNajamuddin\Downloads\data (1).csv")

with col1:
    for index, rows in df[:4].iterrows():
        st.subheader(f'{rows["first name"].title()} {rows["last name"].title()}')
        st.write(rows["role"])
        st.image("images (1)/" + rows["image"])

with col2:
    for index, rows in df[4:8].iterrows():
        st.subheader(f'{rows["first name"].title()} {rows["last name"].title()}')
        st.write(rows["role"])
        st.image("images (1)/" + rows["image"])

with col3:
    for index, rows in df[8:].iterrows():
        st.subheader(f'{rows["first name"].title()} {rows["last name"].title()}')
        st.write(rows["role"])
        st.image("images (1)/" + rows["image"])


