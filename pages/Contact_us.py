import streamlit as st
import pandas as pd
from Send_email import send_email

df = pd.read_csv(r"C:\Users\MNajamuddin\Downloads\Current+State+of+the+Program\topics.csv")


with st.form(key="email address"):
    user_email = st.text_input("your email address")
    # option = st.selectbox(label="What topic do you want to discuss?", options=["Job inquiries", "Business  proposal", "others"])
    option = st.selectbox("What topic you want to discuss", df['topic'])
    raw_message=st.text_area("your message")
    message =f"""\
subject: New email from{user_email}

From: {user_email}
Topic:{option}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        send_email(message)
        st.info("Your email was sent successfully")

